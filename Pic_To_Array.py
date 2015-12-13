#writen by thippo
#python version 3.4.3

def pic_to_array(picfile):
    import numpy as np
    from PIL import Image
    arr=np.asarray(Image.open(picfile))
    return arr