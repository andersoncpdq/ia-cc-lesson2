import os

import cv2
import glob
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os
import numpy as np
import mahotas


def data_augmentation(my_images):
    print(len(my_images))
    #my_images = [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]  # Getting images
    alpha = 1.02
    beta = 0.1
    adjusting_images = [cv2.convertScaleAbs(image, alpha=alpha, beta=beta) for image in my_images]  # Changing the contrast and the brightness of the images
    blur_images = [cv2.medianBlur(image, 1) for image in my_images]  # Images with blur
    rotate_image = [cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) for image in my_images]  # Rotate images
    array = [(my_images[pos], adjusting_images[pos], blur_images[pos], rotate_image[pos]) for pos in range(len(my_images))]
    return array

def otsu_threshold(img):
    # convert to gray image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply blur
    suave = cv2.GaussianBlur(gray, (7,7), 0)
    T = mahotas.thresholding.otsu(suave)
    temp = gray.copy()
    temp[temp > T] = 255
    temp[temp < 255] = 0
    return cv2.bitwise_not(temp)





def preprocessing1(my_images):
    return data_augmentation(my_images)

def preprocessing2(my_images):
    return [otsu_threshold(img) for img in my_images]



def green_channel(img):
    b,g,r = cv2.split(img)
    return g

def preprocessing3(my_images):
    # green channel extraction:
    green_images = [green_channel(img) for img in my_images]

    # CLAHE application:
    clahe_images = [CLAHE(img) for img in green_images]

    # Adaptive Thresholding
    return [adaptive_threshold(img) for img in clahe_images]

def normalize(PATH: str):
    """
    This function will normalize the data between 0 and 1
    :param PATH: Path to files
    :return: image array
    """
    images = [cv2.imread(PATH + '/' + image)/255. for image in os.listdir(PATH)]
    return images


def load_path(path, ext="*"):
    return glob.glob(os.path.join(path, '*'))



def load_images(PATH: str):
    return [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]

def CLAHE(image, clip=2.0, grid=(8,8)):
    """
    Equalizes the histogram of a grayscale image using
    Contrast Limited Adaptive Histogram Equalization (CLAHE).

    :param image: image array
    :param clip: threshold for contrast limiting
    :param grid:  size of grid for histogram equalization
                  (Input image will be divided into equally
                  sized rectangular tiles).

    :return: image array after CLAHE

    """
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=grid)
    return clahe.apply(image)



def resize(img, dim=(224, 224)):
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


    
    

def labeling(data, val):
    return val * np.ones(len(data))

def adaptive_threshold(img, bsize=11, k=2):
    """
    Adaptive threshold is the method where the threshold value is calculated for smaller regions. This leads to
    different threshold values for different regions with regard to the change in lighting. For this, the
    blockSize × blockSize neighborhood was weighted sum of a less constant point.

    :param img: input image matrix (single channel, 8-bit or floating point)
    :param bsize: size of a pixel neighborhood that is used to calculate a threshold value.
    :param k: a constant value that is subtracted from the average or weighted sum of neighborhood pixels.

    :return: adaptive thresholded image array
    """
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, bsize, k)







