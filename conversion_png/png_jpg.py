from PIL import Image
# Adding the GUI interface
# from tkinter import *
import os

# To convert the image From JPG to PNG : {Syntax}
def png_jpg_convert(a):
    img = Image.open(a)
    b = os.path.splitext(a)
    
    png_jpg= b[0]
    png_jpg=png_jpg +'.jpg'
    rgb_im = img.convert('RGB')
    rgb_im.save(png_jpg)


