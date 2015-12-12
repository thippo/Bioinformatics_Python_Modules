def figure_segmentation(figure,size=(168,168),stride=(1,1),out_header='result',out_type='jpg'):
    import numpy as np
    from PIL import Image
    pic=Image.open(figure)
    figure_array=np.array(pic.getdata(),np.uint8).reshape(pic.size[1],pic.size[0],3)
    for i in range(0,figure_array.shape[0]-size[0]+1,stride[0]):
        for j in range(0,figure_array.shape[1]-size[1]+1,stride[1]):
            Image.fromarray(figure_array[i:i+size[0],j:j+size[1]]).save(out_header+'-'+str(i)+'-'+str(j)+'.'+out_type)