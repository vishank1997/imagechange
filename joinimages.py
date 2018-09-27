import cv2
import numpy as np
import os
i = 0
for filename in os.listdir('lowres'):
    img = cv2.imread(os.path.join('lowres', filename))
    img2 = cv2.imread(os.path.join('noisyimg', filename))
    #img3 = cv2.hconcat(img,img2)
    img3 = np.concatenate((img2, img), axis=1)
    cv2.imwrite("./joinedimg/" + filename, img3)