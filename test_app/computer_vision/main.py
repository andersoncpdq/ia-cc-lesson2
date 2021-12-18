import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.layers import Dropout, Flatten, Input, Dense
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import random
import tensorflow as tf
import os
import glob

from src.computer_vision_preproc import *
import cv2
import matplotlib.pyplot as plt
import time

# entrada de dados + redimensionamento:
confluentes = load_path('data_especular_crop/test_images/confluente')
confluentes = confluentes + load_path('data_especular_crop/train_images/confluente')
integras = [path for path in confluentes]

esparsas = load_path('data_especular_crop/test_images/esparsa')
esparsas = esparsas + load_path('data_especular_crop/train_images/esparsa')
esparsas = [path for path in esparsas]

integras = load_path('data_especular_crop/test_images/integra')
integras = integras + load_path('data_especular_crop/train_images/integra')
integras = [path for path in integras]


raras = load_path('data_especular_crop/test_images/rara')
raras = raras + load_path('data_especular_crop/train_images/rara')
raras = [path for path in raras ]


print('confluentes: ', len(confluentes))
print('esparsas: ', len(esparsas))
print('integras: ', len(integras))
print('raras: ', len(raras))

X_path = confluentes + esparsas + integras + raras

print(len(X_path))


X = [np.array(resize(img) for img in load_images(X_path))]
X = data_augmentation(X)
X = np.array(X)
X = X / 255
print(len(X))


