library(magick)

# Imagem
setwd("F:\\Statistics\\Apostila\\eBook\\www\\Imagem")                                       # Local
foto = image_read("vader.jpg")                                                              # Local
foto = image_read("https://github.com/luizleal1974/Editar-Imagem/raw/main/Files/vader.jpg") # URL

# Imagem espelhada
espelho_foto = image_flop(foto)

# Watermark
water_foto = image_annotate(foto,
                            text = "Darth Vader",
                            size = 70,
                            font = "Helvetica",
                            gravity = "southeast",
                            color = "white")

# Salvar imagem
image_write(espelho_foto, path = "vader_mirror.png", format = "png")
image_write(water_foto, path = "vader_watermark.png", format = "png")
