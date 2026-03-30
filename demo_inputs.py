# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:32:45 2022

@author: MME
"""
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import pickle
#from nltk.tokenize import word_tokenize
import tensorflow as tf
import cv2

# Define directories    
images_dir =                 './images_samples/dataset_samples/'   
model_dir  =                 './demo_Inputs/trained_models/'
df_dir =                     './demo_Inputs/data/'
tokenizer_dir  =             './demo_Inputs/data/'

conv1D_fname  =              'Model_Texte_Conv1D.hdf5'
simpleDNN_fname  =           'Model_Texte_SimpleDNN.hdf5'
xception_fname =             'Model_Images_Xception.hdf5'
inception_fname =            'Model_Images_InceptionV3.hdf5'

df_train_sple =              'Xtrain_samples.pkl'
#df_train_sple_cleaned =      'Xtrain_samples_cleaned.pkl'
fitted_tokenizer_name =      'fitted_tokenizer.pickle'

xception_im_shape =          (299, 299)
inception_im_shape =         (299, 299)

xception_SC =                0.66
inception_SC =               0.64
conv1D_SC   =                0.80
simplDNN_SC =                0.81


conv1D_w   =                0.35
simplDNN_w =                0.36
xception_w =                0.29
inception_w =               0.29



# Load Dataframes original train set and cleaned train set - 500 Samples
Xtrain = pd.read_pickle(df_dir+ df_train_sple) # Contains 500 samples 
#Xtrain_cleaned = pd.read_pickle(df_dir + df_train_sple_cleaned) # Contains 1000 samples 

with open(tokenizer_dir + fitted_tokenizer_name, 'rb') as handle:
    fitted_tokenizer = pickle.load(handle)


#  Get an observation randomly
def get_random_row():
    
    row = Xtrain.sample(n=1) # from original 
    row_index =  row.index[0] 
    text_cleaned = row['text']
    im_name = row['image_name'].values[0]
    
    design = row['designation'].values[0]
    descrip = row['description'].values[0] 
    
    if type(descrip) == pd._libs.missing.NAType :      
        descrip = 'NaN' 
    
    return  design, descrip, im_name, text_cleaned, row_index

def get_real_class_info(index):
    
    
    prodcode = Xtrain.loc[Xtrain.index == index]['prdtypecode_org'].values[0]
    label = Xtrain.loc[Xtrain.index == index]['labels'].values[0]
    
    return prodcode, label

# Load Pretrained Models - Conv1D 
@st.cache_resource()
def load_conv1D():
   
    model = load_model(model_dir + conv1D_fname ,  compile = True )    
    return model

# Load Pretrained Models - Simple DNN 
@st.cache_resource()
def load_simpleDNN():
    model = load_model(model_dir + simpleDNN_fname ,  compile = True )
    
    return model

# Load Pretrained Models - Xception 
@st.cache_resource()
def load_xception():
    model = load_model(model_dir + xception_fname ,  compile = True )
    
    return model

# Load Pretrained Models - InceptionV3 
@st.cache_resource()
def load_inception():
    model = load_model(model_dir + inception_fname ,  compile = True )
    
    return model

# Load fitted Tokenizer
def load_tokenizer():
    
    with open(tokenizer_dir + fitted_tokenizer, 'rb') as handle:
         fit_tokenizer = pickle.load(handle)
    return fit_tokenizer

def tokenize_text(input_text):
    maxlen = 400 
    text = fitted_tokenizer.texts_to_sequences(input_text)
    text = tf.keras.preprocessing.sequence.pad_sequences(text,
                                                            maxlen = maxlen,
                                                            padding='post')       
    return text

def prepare_image(image, target):
    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = image/255    
    image = np.expand_dims(image, axis=0)
    return image


#######################################################################################################################################  
#######################################################################################################################################

def predict_with_conv1D(input_text):    
    
    text_tokenized = tokenize_text(input_text)
    model = load_conv1D()
    #model.summary()
    y_pred_proba = model.predict(text_tokenized)
    y_pred_class = np.argmax(y_pred_proba,axis = 1).astype(int)    
    
    # Prediction
    y_pred = y_pred_class[0]
    pred_class = get_class_code(y_pred)
    pred_label = get_label(pred_class)
    

    return str(pred_class) , pred_label , y_pred_proba

def predict_with_simpDNN(input_text):
    

    text_tokenized = tokenize_text(input_text)
    model = load_simpleDNN()

    y_pred_proba = model.predict(text_tokenized)
    y_pred_class = np.argmax(y_pred_proba,axis = 1).astype(int)
    
    
    # Prediction
    y_pred = y_pred_class[0]
    pred_class = get_class_code(y_pred)
    pred_label = get_label(pred_class)
    
 
    return str(pred_class) , pred_label, y_pred_proba

#@st.cache()   
def predict_with_xception(input_image):  
       
        model = load_xception()

        out_proba = model.predict(input_image) # A revoir 
        im_pred= np.argmax(out_proba)        
        # To match with datagenerator labels 
        permutation = [0, 1, 12, 20, 21, 22, 23, 24, 25, 26, 2, 3,
                 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16
                 ,17, 18, 19]
        
        out_proba = out_proba[:, permutation] 
        
        im_pred_target = get_real_target(im_pred)
        im_pred_code = get_class_code(im_pred_target)
        im_pred_label = get_label(im_pred_code)

        return im_pred_code ,im_pred_label, out_proba


#@st.cache() 
def predict_with_inception(input_image):    

        model = load_inception()

        out_proba = model.predict(input_image) # A revoir 
        im_pred= np.argmax(out_proba)
        
        # To match with datagenerator labels 
        permutation = [0, 1, 12, 20, 21, 22, 23, 24, 25, 26, 2, 3,
                 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16
                 ,17, 18, 19]
        
        out_proba = out_proba[:, permutation] 
        
        im_pred_target = get_real_target(im_pred)
        im_pred_code = get_class_code(im_pred_target)
        im_pred_label = get_label(im_pred_code)

        return im_pred_code ,im_pred_label,out_proba


#@st.cache()   
@st.cache_resource()
def predict_with_xception_manu(source_image): 
    
        model = load_xception()

        out_proba = model.predict(source_image)
        im_pred= np.argmax(out_proba)
        
        # To match with datagenerator labels 
        permutation = [0, 1, 12, 20, 21, 22, 23, 24, 25, 26, 2, 3,
                 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16
                 ,17, 18, 19]
        
        out_proba = out_proba[:, permutation] 
        
        im_pred_target = get_real_target(im_pred)
        im_pred_code = get_class_code(im_pred_target)
        im_pred_label = get_label(im_pred_code)

        return im_pred_code ,im_pred_label, out_proba 
    
#######################################################################################################################################  
#######################################################################################################################################
# @st.cache() 
st.cache_data()
def predict_with_inception_manu(source_image): 
    
        model = load_inception()

        out_proba = model.predict(source_image)
        im_pred= np.argmax(out_proba)
        
        # To match with datagenerator labels 
        permutation = [0, 1, 12, 20, 21, 22, 23, 24, 25, 26, 2, 3,
                 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16
                 ,17, 18, 19]
        
        out_proba = out_proba[:, permutation] 
        
        im_pred_target = get_real_target(im_pred)
        im_pred_code = get_class_code(im_pred_target)
        im_pred_label = get_label(im_pred_code)

        return im_pred_code ,im_pred_label, out_proba   

 
#######################################################################################################################################
#######################################################################################################################################  
def predict_conv1D_simp_DNN_xception(input_text, input_image):
   
        pred_class_conv1D , pred_label_conv1D  , y_pred_proba_conv1D  = predict_with_conv1D(input_text)
        pred_class_simp , pred_label_simp  , y_pred_proba_simp        = predict_with_simpDNN(input_text)
        im_pred_code ,im_pred_label, out_proba_cnn                    = predict_with_xception(input_image)       
        
        weighted_proba = ((y_pred_proba_conv1D * conv1D_SC) + (y_pred_proba_simp * simplDNN_SC) + (out_proba_cnn * xception_SC)) / (conv1D_SC + simplDNN_SC + xception_SC)


        y_pred_class = np.argmax(weighted_proba,axis = 1).astype(int)  
        
        y_pred = y_pred_class[0]
        pred_class = get_class_code(y_pred)
        pred_label = get_label(pred_class)
        proba = np.amax(weighted_proba) 


        return pred_class ,pred_label, proba
    
def predict_conv1D_simp_DNN_xception_manu(input_text, source_image):
   
        pred_class_conv1D , pred_label_conv1D  , y_pred_proba_conv1D  = predict_with_conv1D(input_text)
        pred_class_simp , pred_label_simp  , y_pred_proba_simp        = predict_with_simpDNN(input_text)
        im_pred_code ,im_pred_label, out_proba_cnn                    = predict_with_xception_manu(source_image)       
        
        weighted_proba = ((y_pred_proba_conv1D * conv1D_SC) + (y_pred_proba_simp * simplDNN_SC) + (out_proba_cnn * xception_SC)) / (conv1D_SC + simplDNN_SC + xception_SC)


        y_pred_class = np.argmax(weighted_proba,axis = 1).astype(int)  
        
        y_pred = y_pred_class[0]
        pred_class = get_class_code(y_pred)
        pred_label = get_label(pred_class)
        proba = np.amax(weighted_proba) 


        return pred_class ,pred_label, proba
    
def predict_conv1D_simp_DNN_inception_manu(input_text, source_image):
   
    
        pred_class_conv1D , pred_label_conv1D  , y_pred_proba_conv1D  = predict_with_conv1D(input_text)
        pred_class_simp , pred_label_simp  , y_pred_proba_simp        = predict_with_simpDNN(input_text)
        im_pred_code ,im_pred_label, out_proba_cnn                    = predict_with_inception_manu(source_image)       
        
        weighted_proba = ((y_pred_proba_conv1D * conv1D_SC) + (y_pred_proba_simp * simplDNN_SC) + (out_proba_cnn * inception_SC)) / (conv1D_SC + simplDNN_SC + inception_SC)


        y_pred_class = np.argmax(weighted_proba,axis = 1).astype(int)  
        
        y_pred = y_pred_class[0]
        pred_class = get_class_code(y_pred)
        pred_label = get_label(pred_class)
        proba = np.amax(weighted_proba) 


        return pred_class ,pred_label, proba 
def predict_conv1D_simp_DNN_inception(input_text, input_image):   
    
    
        pred_class_conv1D , pred_label_conv1D  , y_pred_proba_conv1D  = predict_with_conv1D(input_text)
        pred_class_simp , pred_label_simp  , y_pred_proba_simp        = predict_with_simpDNN(input_text)
        im_pred_code ,im_pred_label, out_proba_cnn                    =  predict_with_inception(input_image)      
        
        weighted_proba = ((y_pred_proba_conv1D * conv1D_SC) + (y_pred_proba_simp * simplDNN_SC) + (out_proba_cnn * inception_SC)) / (conv1D_SC + simplDNN_SC + inception_SC)

        y_pred_class = np.argmax(weighted_proba,axis = 1).astype(int)  
        
        y_pred = y_pred_class[0]
        pred_class = get_class_code(y_pred)
        pred_label = get_label(pred_class)
        proba = np.amax(weighted_proba) 


        return pred_class ,pred_label, proba
    
 
    
def get_class_code(val):
    dict_class =       {0:10, 1:40, 2:50, 3:60, 4:1140,
                        5:1160, 6:1180, 7:1280, 8:1281,
                        9:1300, 10:1301, 11:1302, 12:1320,
                        13:1560, 14:1920, 15:1940, 16:2060,
                        17:2220, 18:2280, 19:2403, 20:2462,
                        21:2522, 22:2582, 23:2583, 24:2585,
                        25:2705, 26:2905,
                        }   
    return dict_class[val]
    dict_class =       {0:10, 1:40, 2:50, 3:60, 4:1140,
                        5:1160, 6:1180, 7:1280, 8:1281,
                        9:1300, 10:1301, 11:1302, 12:1320,
                        13:1560, 14:1920, 15:1940, 16:2060,
                        17:2220, 18:2280, 19:2403, 20:2462,
                        21:2522, 22:2582, 23:2583, 24:2585,
                        25:2705, 26:2905,
                        }   
    return dict_class[val]


def get_label(code):
    dict_code_label =  { 50: 'video games accessories',
                         2705: 'books',
                         2522: 'stationery',
                         2582: 'furniture kitchen and garden',
                         1560: 'interior furniture and bedding',
                         1281: 'board games',
                         1920: 'interior accessories',
                         1280: 'toys for children',
                         1140: 'figurines and Toy Pop',
                         1300: 'remote controlled models',
                         2060: 'decoration interior',
                         2583: 'piscine spa',
                         60: 'games and consoles',
                         1320: 'early childhood',
                         2280: 'magazines',
                         1302: 'toys, outdoor playing, clothes',
                         2220: 'supplies for domestic animals',
                         40: 'imported video games',
                         2905: 'online distribution of video games',
                         2585: 'gardening and DIY',
                         1940: 'Food',
                         1160: 'playing cards',
                         1301: 'accessories children',
                         10: 'adult books',
                         1180: 'figurines, masks and role playing games',
                         2403: 'children books and magazines',
                         2462: 'games'}
   
    return dict_code_label[code]

def get_real_target(val):
    
    dict_labels = {'0': 0,
                 '1': 1,
                 '10': 2,
                 '11': 3,
                 '12': 4,
                 '13': 5,
                 '14': 6,
                 '15': 7,
                 '16': 8,
                 '17': 9,
                 '18': 10,
                 '19': 11,
                 '2': 12,
                 '20': 13,
                 '21': 14,
                 '22': 15,
                 '23': 16,
                 '24': 17,
                 '25': 18,
                 '26': 19,
                 '3': 20,
                 '4': 21,
                 '5': 22,
                 '6': 23,
                 '7': 24,
                 '8': 25,
                 '9': 26}
        
    
    for real_cls, gen_label in dict_labels.items():
         if val == gen_label:
            return int(real_cls)

    return "class doesn't exist"

#********************************************************************************

