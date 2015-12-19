def cosine(a,b):
    import numpy as np
    a=np.asarray(a)
    b=np.asarray(b)
    la=np.sqrt(a.dot(a))
    lb=np.sqrt(b.dot(b))
    return a.dot(b)/(la*lb)