import os
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Input, Dense, BatchNormalization
from tensorflow.keras.models import Sequential
from src.computer_vision_preproc import *


def main():

    gen_train_augmentation = ImageDataGenerator(rescale=1./255, horizontal_flip=True, rotation_range=7, zoom_range=0.2)
    gen_test_augmentation = ImageDataGenerator(rescale=1./255)
    base_train = gen_train_augmentation.flow_from_directory('./data_especular_crop/train_images/', target_size=(224, 224), class_mode='categorical')
    base_test = gen_test_augmentation.flow_from_directory('./data_especular_crop/test_images/', target_size=(224, 224), class_mode='categorical')

    base_train = to_categorical(base_train, 4)
    base_test = to_categorical(base_test, 4)

    classifier = Sequential()
    classifier.add(Conv2D(64, (5, 5), activation='relu', input_shape=(224, 224, 3)))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Conv2D(64, (5, 5), activation='relu', input_shape=(224, 224, 3)))
    classifier.add(BatchNormalization())
    classifier.add(MaxPooling2D())
    classifier.add(Conv2D(64, (5, 5), activation='relu', input_shape=(224, 224, 3)))
    classifier.add(Dropout(0.2))
    classifier.add(Dense(units=128, activation='relu'))
    classifier.add(Dropout(0.2))

    classifier.compile(optimizer='adam', loss='categorical_crossentropy',
                       metrics=['accuracy'], )
    classifier.fit_generator(base_train, steps_per_epoch=int(1306/32), epochs=5,
                             validation_data=base_test, validation_steps=434/32)

main()








