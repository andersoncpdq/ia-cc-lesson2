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
# glob.glob("<your image directory path>\\*.png"):
#confluentes = glob.glob("data_especular_crop\\train_images\\confluente\\*.png")
#confluentes = confluentes + glob.glob(os.path.join('data_especular_crop/test_images/confluente', '*'))
#confluentes = [path for path in confluentes]

#esparsas = glob.glob(os.path.join('data_especular_crop/train_images/esparsa', '*'))
#esparsas = esparsas + glob.glob(os.path.join('data_especular_crop/test_images/esparsa', '*'))
#esparsas = [path for path in esparsas]

#glob.glob("<your image directory path>\\*.png"):
integras = glob.glob("data_especular_crop\\train_images\\integra\\*.png")
integras = integras + glob.glob("data_especular_crop\\test_images\\integra\\*.png")
#integras = sorted(os.listdir('data_especular_crop/train_images/integra'))
#integras = integras + sorted(os.listdir('data_especular_crop/test_images/integra'))
integras = [path for path in integras]

#raras = glob.glob(os.path.join('data_especular_crop/train_images/rara', '*'))
#raras = raras + glob.glob(os.path.join('data_especular_crop/test_images/rara', '*'))
#raras = [path for path in raras]

#print('confluentes: ', len(confluentes))
#print('esparsas: ', len(esparsas))
print('integras: ', len(integras))
#print('raras: ', len(raras))

#X_path = confluentes + esparsas + integras + raras
X_path = integras
print(len(X_path))

X = [np.array(resize(path)) for path in X_path]
X = np.array(X)
X = X / 255

img = cv2.imread(integras[1])
print(img.shape)