#writen by thippo
#python version 3.4.3

import numpy as np
from PIL import Image

def pic_to_array(picfile):
    bug=Image.open(picfile)
    arr=np.array(bug.getdata(),np.uint8).reshape(bug.size[1],bug.size[0],3)
	return arr
