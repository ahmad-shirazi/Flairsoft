import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from sklearn.cluster import spectral_clustering
from sklearn.feature_extraction import image
import cv2

def denoise(image):
    imga = cv2.imread(image, 0)

    img = 255 - np.uint8(imga)
    kernel = np.ones((3, 3), np.uint8)
    
    # Using cv2.erode() method 
    image1 = cv2.erode(img, kernel) 
    image = cv2.erode(image1, kernel) 
    # image = cv2.dilate(img, kernel) 
    
    # Displaying the image 
    data = 255 - np.uint8(image)
    kernel = np.array([[-1, -1, -1],
                    [-1, 9,-1],
                    [-1, -1, -1]])
    image_sharp = cv2.filter2D(src=data, ddepth=-1, kernel=kernel)
    # cv2.imshow(data)
    # cv2.imshow(255-image1)
    dnimage = cv2.imwrite('dnimage.png', img)
    return dnimage


