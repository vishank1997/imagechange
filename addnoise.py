import cv2
import numpy as np
import os
i = 0
for filename in os.listdir('lowres'):
	img = cv2.imread(os.path.join('lowres',filename))
	row,col,ch= img.shape
	i = i+1

	print(i)
	mean = 0
	var = 0.1
	sigma = var**0.5
	gauss = np.random.normal(mean,sigma,(row,col,ch))
	#print(gauss)
	gauss = gauss*60

	gauss = gauss.reshape(row,col,ch)

	img = img + gauss
	cv2.imwrite( "./noisyimg/"+filename, img )
	#cv2.imshow(filename, img)