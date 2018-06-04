import sys
import tensorflow as tf
from PIL import Image,ImageFilter

def leInteiro(imvalue):
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)

    init_op = tf.global_variables_initializer()
    saver = tf.train.Saver()
    
	
	# Carrega o modelo salvo na pasta e usa o conhecimento salvo pra poder "adivinhar o número"
    with tf.Session() as sess:
        sess.run(init_op)
        saver.restore(sess, "modelo.ckpt")
   
        prediction=tf.argmax(y,1)
        return prediction.eval(feed_dict={x: [imvalue]}, session=sess)


def preparaImagem(argv):
	#Salva a imagem, passada como argumento de linha de comando, em pixels 
    imagemAdvinhar = Image.open(argv).convert('L')
    width = float(imagemAdvinhar.size[0])
    height = float(imagemAdvinhar.size[1])
    newImage = Image.new('L', (28, 28), (255)) #Cria uma imagem em branco de 28 x 28
    
    if width > height: #Verifica qual dimensão é maior
        nheight = int(round((20.0/width*height),0)) #Ajuta a altura
		
		# Redimensiona os pixels.
        img = iimagemAdvinharm.resize((20,nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight)/2),0)) #Calcula posição horizontal
        newImage.paste(img, (4, wtop)) #Cola imagem na tela em branco
    else:
        nwidth = int(round((20.0/height*width),0)) #Ajuta a largura
		
		# Redimensiona os pixels.
        img = im.resize((nwidth,20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth)/2),0)) #Calcula posição vertical
        newImage.paste(img, (wleft, 4)) #Cola imagem na tela em branco
    

    tv = list(newImage.getdata()) #Lista o valor dos pixels.
    
    #Transforma tudo em preto 1 ou branco 0
    tva = [ (255-x)*1.0/255.0 for x in tv] 
    return tva

def main(argv):
    imvalue = preparaImagem(argv)
    valorInteiro = leInteiro(imvalue)
    print (valorInteiro[0]) #primeiro valor da lista
    
if __name__ == "__main__":
    main(sys.argv[1])
