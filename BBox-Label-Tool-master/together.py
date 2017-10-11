from collections import deque
import numpy as np
import cv2
import os
from os import listdir
from os.path import isfile, join
########edit this!!!!!
class_name = 'UAV' # plane heli bird
########
file_names = [ f for f in listdir('./Labels/001') if isfile(join(r'./Labels/001',f)) ]
if file_names[0] == '.DS_Store':
    del file_names[0]
#print file_names
start_matrix = [['xmin', 'ymin', 'xmax', 'ymax', 'image_name', 'class']]
for i in range(len(file_names)):
    if file_names[i] != 'test.txt':
        textfile_name = file_names[i]
        label_matrix = np.loadtxt(os.path.join('./Labels/001', textfile_name),dtype='str')
        dim = label_matrix.shape
        if dim[0] == 0:
            continue
        if len(dim) == 1:
            label_matrix = label_matrix.reshape((1,dim[0]))
        print textfile_name
        dim_new = label_matrix.shape
        column_vec = np.zeros(shape=(dim_new[0],)).astype(np.str)
        #image_name = textfile_name[0:-3] + 'jpg'
        column_vec[:,] = textfile_name
        new_matrix = np.zeros(shape=(dim_new[0],6)).astype(np.str)
        new_matrix[:,0:4] = label_matrix[:,0:4]
        new_matrix[:,4] = column_vec
        new_matrix[:,5] = label_matrix[:,4]
        start_matrix = np.row_stack((start_matrix,new_matrix))
print start_matrix
fmt='%s %s %s %s %s %s'
np.savetxt('label.txt', start_matrix, fmt = fmt)
