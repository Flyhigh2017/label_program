import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

data_path = '/Users/anekisei/Documents/BBox-Label-Tool-master/Images'
image_path = join(data_path, '001')
file_names = [ f for f in listdir(image_path) if isfile(join(image_path,f)) ]
file_names = np.array(file_names)
file_names = file_names.reshape((-1,1))
fmt='%s'
np.savetxt('name.txt', file_names, fmt = fmt)
#cv2.imshow('result',raw_image)


'''
https://stackoverflow.com/questions/24536552/how-to-combine-pywavelet-and-opencv-for-image-processing
https://stackoverflow.com/questions/5707353/how-to-extend-pywavelets-to-work-with-n-dimensional-data
'''







