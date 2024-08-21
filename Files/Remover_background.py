from rembg import remove
from PIL import Image
from urllib.request import urlopen

# Imagem
foto = Image.open(urlopen('https://github.com/luizleal1974/Editar-Imagem/raw/main/Files/woman_model.png'))

# Remover background
foto_no_bg = remove(foto)

# Salvar imagem 
foto_no_bg.save('vader_no_bg.png')
