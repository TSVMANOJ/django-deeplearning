import tensorflow as tf
from tensorflow import keras
from keras.models import Model
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2



def MlModel(x):
    img_arr=cv2.imread(x,0)
    #print("******************MLMODEL")
    #print(img_arr)
    #img_arr=cv2.resize(img_arr,(28,28))
    #img_arr= img_arr.reshape(-1,28,28,1)
    #print(img_arr)
    #print(img_arr.shape)
    new_model = load_model(r'aslapp\modeloutput.h5')
    temp=new_model.predict(img_arr)
    #return temp
    #print(temp)
    l=list(temp)
    index=0
    dic={}
    """
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j]:
                  index=j
                  break
                  """

    c='A'              
    for i in range(25):
        if i==9:
            c=chr(ord(c)+1)
            continue
        dic[i]=c 
        c=chr(ord(c)+1)
    index=0   
    
    for i in range(len(l)):
        for j in range(len(l[0])):
            if (l[i][j] == 0 ):
                continue
            else  :
                if(j>=9) :
                 index=j+1    
                 break 

                
        
    print(index)    
    print(temp)    
    print(dic[index])   
    
               


  
def mazak(hi):
    MlModel(hi)
    



