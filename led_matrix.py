from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import settings

def init():
    options = RGBMatrixOptions()
    options.rows = settings.npix
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options = options)
    return matrix

def show(a, matrix):
    image = Image.new("RGB", (settings.npix, settings.npix)) 
    draw = ImageDraw.Draw(image) 
    for i in range(n):
        for j in range(n):
            r = int(200*a[j,i,0])
            g = int(200*a[j,i,1])
            b = int(200*a[j,i,2])
            draw.rectangle((i, j, i+1, j+1), fill=(r, g, b))
    matrix.Clear()
    matrix.SetImage(image)
