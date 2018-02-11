import numpy as np

some_val = 0
some_other_val = 0

image = np.random.random((10,10))
origin = [some_val,some_other_val]

def distanceMat(image, origin):
    y,x = np.mgrid[:image.shape[0],:image.shape[1]].astype(float)    
    #r = [ np.sqrt((x1-origin[0])**2 + (y1-origin[1])**2) for x1,y1 in zip (y,x)]
    r = np.hypot(y-origin[0],x-origin[1])
    print r
    return r


r = distanceMat(image, origin)
