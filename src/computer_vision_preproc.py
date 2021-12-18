import os

import cv2
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os


def data_augmentation(my_images):
   # my_images = [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]  # Getting images
    print(my_images)
    alpha = 1.02
    beta = 0.1
    adjusting_images = [cv2.convertScaleAbs(image, alpha=alpha, beta=beta) for image in my_images]  # Changing the contrast and the brightness of the images
    blur_images = [cv2.medianBlur(image, 1) for image in my_images]  # Images with blur
    rotate_image = [cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) for image in my_images]  # Rotate images
    array = [(my_images[pos], adjusting_images[pos], blur_images[pos], rotate_image[pos]) for pos in range(len(my_images))]
    return array


def normalize(PATH: str):
    """
    This function will normalize the data between 0 and 1
    :param PATH: Path to files
    :return: image array
    """
    images = [cv2.imread(PATH + '/' + image)/255. for image in os.listdir(PATH)]
    return images







