import os

import cv2
import glob
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os
import numpy as np

IMGS = sorted(os.listdir('/home/bagriel/IAAcademy/iaacademy-cc/test_app/computer_vision/data_especular_crop/test_images/confluente'))


def data_augmentation():
    my_images = [cv2.imread('/home/bagriel/IAAcademy/iaacademy-cc/test_app/computer_vision/data_especular_crop/test_images/confluente' + f'/{image}') for image in IMGS]  # Getting images
    print(my_images)
    alpha = 1.02
    beta = 0.1
    adjusting_images = [cv2.convertScaleAbs(image, alpha=alpha, beta=beta) for image in my_images]  # Changing the contrast and the brightness of the images
    blur_images = [cv2.medianBlur(image, 1) for image in my_images]  # Images with blur
    rotate_image = [cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) for image in my_images]  # Rotate images
    array = [(my_images[pos], adjusting_images[pos], blur_images[pos], rotate_image[pos]) for pos in range(len(my_images))]

    return array


def preprocessing1(PATH: str):
    pass

def preprocessing2(PATH: str):
    pass

def green_channel(img):
    b,g,r = cv2.split(img)
    return g


def preprocessing3(PATH: str):
    # green channel extraction:

    # CLAHE application:

    # Adaptive Thresholding

    pass


def normalize(images):
    """
    This function will normalize the data between 0 and 1
    :param images: array of images
    :return: image array
    """
    new_image = []
    for index in range(len(images)):
        new_image.append(images[index]/255.)

    return new_image




def load_path(path, ext="*"):
    return os.path.join(path, ext)


def load_images(paths):
    return [cv2.imread(path) for path in paths]

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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=grid)
    return clahe.apply(gray)



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







