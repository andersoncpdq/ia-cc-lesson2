import os

import cv2
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
import os


def data_augmentation(PATH: str):
    my_images = [cv2.imread(PATH + '/' + image) for image in sorted(os.listdir(PATH))]  # Getting images
    print(my_images)
    alpha = 1.02
    beta = 0.1
    adjusting_images = [cv2.convertScaleAbs(image, alpha=alpha, beta=beta) for image in my_images]  # Changing the contrast and the brightness of the images
    blur_images = [cv2.medianBlur(image, 1) for image in my_images]  # Images with blur
    rotate_image = [cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE) for image in my_images]  # Rotate images
    for image in rotate_image:  # Testing new arrays
        while True:
            cv2.imshow(f'image', image)
            key = cv2.waitKey(1)
            if key == ord('q'):  # Press 'q' to pass to next image
                break


data_augmentation('PATH HERE')





