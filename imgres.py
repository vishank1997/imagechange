import cv2
import numpy as np
import os
i = 0
for filename in os.listdir("images dataset to be noised"):
	img = cv2.imread(os.path.join('images dataset to be noised',filename))
	#row,col,ch= img.shape
	i = i+1

	#print(i)
	#mean = 0
	#var = 0.1
	#sigma = var**0.5
	#gauss = np.random.normal(mean,sigma,(row,col,ch))
	#print(gauss)
	#gauss = gauss*60

	#gauss = gauss.reshape(row,col,ch)

	img = cv2.resize(img, (510,339))
	cv2.imwrite( "./lowres/"+filename, img )
	#cv2.imshow(filename, img)