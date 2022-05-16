import numpy as np

for i in range(-4,4):
    del_x = np.sqrt((10**i)/8000)
    print('i : {:<10}    : {:<8.5f}   ({:8.4f}%)'.format(i, del_x, 100*del_x/4))