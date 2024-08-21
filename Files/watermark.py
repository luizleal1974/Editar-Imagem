from os import chdir
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen

# Imagem
chdir("F:\Statistics\Apostila\eBook\www\Imagem")                                                     # Local
foto = Image.open('vader.jpg')                                                                       # Local
foto = Image.open(urlopen('https://github.com/luizleal1974/Editar-Imagem/raw/main/Files/vader.jpg')) # URL

# Texto e fonte
text = "Darth Vader"
font = ImageFont.truetype("arial.ttf", 70)

# Dimensões
draw = ImageDraw.Draw(foto)
width, height = foto.size             # Da imagem original
tamanho = draw.textlength(text, font) # Do texto

# Coordenadas da marca d'água
margin = 10
x = width - tamanho + 0.1 * margin
y = height - tamanho + 29.5 * margin

# Marca d'água
draw.text((x, y), "Darth Vader", (255, 255, 255), font = font)
foto.save('vader_watermark.png')
