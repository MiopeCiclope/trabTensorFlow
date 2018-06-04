1. criarModelo.py – Cria um modelo de rede neural e treina para compreender imagens escritas a mão.
2. leImagem.py – Usa o modelo criado para ler imagens escritas a mão de um arquivo .png.

#Como Usar
Apos intaladas dependências descritas no turorial https://www.tensorflow.org/install/

#1. Criar o modelo
Navegue pelo terminal até a pasta de instalação do python e execute o seguinte comando:

"python <Caminho absoluto do arquivo>\criarModelo.py"

para criar um modelo baseado no MNIST.

#2. Crie um arquivo de imagem
Abra o paint e escreva um número com o pincel, utilizando o fundo branco e a cor preta para escrever o número.
OBS: O MNIST usa como base arquivos de imagem de tamanho 28 x 28 pixels para treinar a rede, porém o script lerImagem.py ajusta a imagem para o tamanho específico, podendo então gerar algumas perdas e dificultar a predição caso o ajuste distorça a imagem.

#3. Deixe o script "adivinhar" seu número
Navegue pelo terminal até a pasta de instalação do python e execute o seguinte comando:

"python <Caminho absoluto do arquivo>\leImagem.py <Caminho absoluto do arquivo>\imagemDoNumero.png"



