#writen by thippo
#python version 3.4.3

def pic_to_array(picfile):
    import numpy as np
    from PIL import Image
    pic=Image.open(picfile)
    arr=np.array(pic.getdata(),np.uint8).reshape(pic.size[1],pic.size[0],3)
    return arr