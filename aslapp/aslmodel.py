import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 
import pandas as pd 

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout , BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix



train= pd.read_csv("sign_mnist_train.csv")
test=pd.read_csv("sign_mnist_train.csv")

labels = train['label'].values

unique_values = np.array(labels)
np.unique(unique_values)


train_label=train['label']  
trainset=train.drop(['label'],axis=1)

x_train = trainset.values.reshape(-1,28,28,1)

test_label=test['label']
x_test=test.drop(['label'],axis=1)

x_test=x_test.values.reshape(-1,28,28,1)


x_train = x_train / 255
x_test = x_test / 255





