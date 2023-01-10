import glob
from PIL import Image
import os 

# filepaths
def png_gif_convert(a):
    
    fp_in = a
    b = os.path.splitext(a)
    
    jpg_gif= b[0]
    jpg_gif=jpg_gif+'.gif'
    fp_out = jpg_gif

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
    img = next(imgs)  # extract first image from iterator
    
    img.save(fp=fp_out, format='GIF', append_images=imgs,
            save_all=True, duration=200, loop=0)
    
    
    
# if __name__=="__main__":
#     png_gif_convert()