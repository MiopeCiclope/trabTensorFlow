import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Importa os dados do MNIST
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Cria o modelo
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)

# Define perdas e otimizadores
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init_op = tf.global_variables_initializer()
saver = tf.train.Saver()

# Treina e salva o modelo no mesmo diretoria onde o scipt foi iniciado
with tf.Session() as sess:
    sess.run(init_op)
	# Treina o modelo usando o número de imagens passadas na função range e imprime uma mensagem com a porcentagem
	# de sucesso a cada 100 imagens usadas.
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
        
    save_path = saver.save(sess, "./modelo.ckpt")
	
print("Modelo treinado com sucesso")

