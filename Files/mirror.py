from os import chdir
from PIL import Image
from urllib.request import urlopen

# Imagem
chdir("F:\Statistics\Apostila\eBook\www\Imagem")                                                     # Local
foto = Image.open('vader.jpg')                                                                       # Local
foto = Image.open(urlopen('https://github.com/luizleal1974/Editar-Imagem/raw/main/Files/vader.jpg')) # URL

# Imagem "espelhada"
espelho_foto = foto.transpose(Image.FLIP_LEFT_RIGHT)

# Salvar imagem 
espelho_foto.save('vader_mirror.png')
