from PIL import Image

import os

# To convert the image From JPG to PNG : {Syntax}
def jpg_png_convert(a):
    img = Image.open(a)
    b = os.path.splitext(a)
    
    jpg_png= b[0]
    jpg_png=jpg_png +'.png'
    
    img.save(jpg_png)


