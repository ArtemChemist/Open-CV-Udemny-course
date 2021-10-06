import os
os.chdir("/home/artem/Source Code/Open CV Udemny course")
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
seedvalue = 123
np.random.seed(seedvalue)
exec(open(os.path.abspath('image_common_utils.py')).read())
img_path = './image_data/elephant.png'


from skimage import data
cmr = data.camera()



nrows, ncols = cmr.shape




row, col = np.ogrid[:nrows, :ncols] 

print(row.shape)
print( col.shape)
len(row), len(col[0])

cnt_row, cnt_col = nrows / 2, ncols / 2
outer_disk_mask = ((row - cnt_row)**2 + (col - cnt_col)**2 > (nrows / 2)**2)
print(outer_disk_mask )
cmr[outer_disk_mask] = 0

plt.imshow(cmr, cmap=plt.get_cmap('gray'))
plt.show()


