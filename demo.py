from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

PI = True

if PI:
    px = 1 
    from rgbmatrix import RGBMatrix, RGBMatrixOptions
    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    matrix = RGBMatrix(options = options)
else:
    px = 20

image = Image.new("RGB", (32*px, 32*px))
draw = ImageDraw.Draw(image)

def display(a):
    for i in range(32):
        for j in range(32):
            r = int(255*a[i,j,0])
            g = int(255*a[i,j,1])
            b = int(255*a[i,j,2])
            draw.rectangle((i*px, j*px, (i+1)*px, (j+1)*px), fill=(r, g, b))
    if PI:
        matrix.SetImage(image.convert('RGB'))
    else:
        image.show()

a = np.zeros((32,32,3))
for i in range(8):
    for j in range(8):
        for c in range(3):
            a[i, j, c] = random.random()
display(a)
