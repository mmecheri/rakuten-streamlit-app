# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:30:24 2022

@author: MME
"""
import streamlit as st
import  demo_inputs
import  cleaning_text  
from PIL import Image
from io import BytesIO
import numpy as np
import cv2


def app():
   
    
    st.title("Predictions (Demo)")
    contenent_page(text_page ='./page_descriptions/demo_txt.md')


def contenent_page(text_page):
    
    '''The text page. Read from .md file '''
    with open(text_page, 'r', encoding='utf-8') as txtpage: 
        txtpage = txtpage.read().split('---Insersetion---')
        
        st.markdown(txtpage[0], unsafe_allow_html=True) 

     
        classif_options = st.selectbox(
        'Please select a classification type',
          (['', 'From Text', 'From Images', 'From Text and Images (Bimodal)']))
    
        
        if classif_options != '':
                
            if classif_options == 'From Text':
                st.markdown(txtpage[1], unsafe_allow_html=True)                           
                models_txt_options = st.selectbox(
                  'Please select a model',
                  (['','Conv1D', 'Simple DNN']))
            
                
            elif classif_options == 'From Images':
                st.markdown(txtpage[1], unsafe_allow_html=True) 
                models_img_options = st.selectbox(
                  'Please select a model',
                  (['', 'Xception', 'InceptionV3']))
              
                
            elif classif_options == 'From Text and Images (Bimodal)':
                    st.markdown(txtpage[1], unsafe_allow_html=True) 
                    models_bimod_options = st.selectbox(
                      'Please select a combination',
                      (['', 'Conv1D & Simple DNN & Xception', 'Conv1D & Simple DNN & InceptionV3']))
                                    
               
            st.markdown(txtpage[2], unsafe_allow_html=True)                    

            # source_options = st.selectbox(
            #           'Please select a data source',
            #           (['', 'Sample from training dataset (Random Choice)', 'Manual' ]))
            

     
#***************************************************************************************************************************** 
#------------------------------------------ # From the training dataset (Random Sample)-------------------------
#*****************************************************************************************************************************          
            # if  classif_options == 'From Text' and models_txt_options == 'Conv1D':
              # if  source_options == 'Sample from training dataset (Random Choice)':
           
              #     if st.button('Get an example and Classify'): 
              #         design, descrip, im_name, text_cleaned, row_index = demo_inputs.get_random_row()
                                        
              #         st.text_input('Designation', design, disabled = True)
              #         st.text_input('Description', descrip, disabled = True)
                                    
              #         pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_conv1D(text_cleaned)                    
              #         prodcode, label = demo_inputs.get_real_class_info(row_index)
                      
              #         col1, col2 = st.columns(2)

              #         with col1: 
              #             msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #             msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                    
              #             precision = np.amax(y_pred_proba)
              #             precision = precision * 100
              #             precision = np.round(precision,2)
                        
              #             msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #             st.markdown(msg1, unsafe_allow_html=True)
              #             st.markdown(msg2, unsafe_allow_html=True) 
              #             st.markdown(msg3, unsafe_allow_html=True) 
                                      
              #         with col2:                       
              #             msg4 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
              #             msg5 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
              #             st.markdown(msg4, unsafe_allow_html=True) 
              #             st.markdown(msg5, unsafe_allow_html=True) 
                          
# #****************************************************************************************************************                  
            # if  classif_options == 'From Text' and models_txt_options == 'Simple DNN':
              # if  source_options == 'Sample from training dataset (Random Choice)':                   
                   
              #     if st.button('Get an example and Classify'): 
              #         design, descrip, im_name, text_cleaned,row_index = demo_inputs.get_random_row()
                                                  
              #         st.text_input('Designation', design, disabled = True)
              #         st.text_input('Description', descrip, disabled = True)
                              
              #         pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_simpDNN(text_cleaned) 
              #         prodcode, label = demo_inputs.get_real_class_info(row_index)
              
              #         col1, col2 = st.columns(2)

              #         with col1: 
              #           msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #           msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                    
              #           precision = np.amax(y_pred_proba)
              #           precision = precision * 100
              #           precision = np.round(precision,2)
                    
              #           msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #           st.markdown(msg1, unsafe_allow_html=True)
              #           st.markdown(msg2, unsafe_allow_html=True) 
              #           st.markdown(msg3, unsafe_allow_html=True) 
                            
              #         with col2:                       
              #           msg4 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
              #           msg5 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
              #           st.markdown(msg4, unsafe_allow_html=True) 
              #           st.markdown(msg5, unsafe_allow_html=True)
                                  
# #****************************************************************************************************************            
            # if  classif_options == 'From Images' and models_img_options == 'Xception':
              # if  source_options == 'Sample from training dataset (Random Choice)':
             
              #     if st.button('Get an example and Classify'): 

              #       design, descrip, im_name, text_cleaned, row_index = demo_inputs.get_random_row()
                
              #       image = Image.open(demo_inputs.images_dir + im_name)
              #       st.image(image, channels="BGR",width=299,caption= im_name)

              #       image = demo_inputs.prepare_image(image, target=(299, 299))
                    
              #       pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_xception(image)
              #       prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
              #       col1, col2 = st.columns(2)

              #       with col1: 
              #         msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #         msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                    
              #         precision = np.amax(y_pred_proba)
              #         precision = precision * 100
              #         precision = np.round(precision,2)
                    
              #         msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #         st.markdown(msg1, unsafe_allow_html=True)
              #         st.markdown(msg2, unsafe_allow_html=True) 
              #         st.markdown(msg3, unsafe_allow_html=True) 
                                  
              #       with col2:                       
              #         msg4 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
              #         msg5 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
              #         st.markdown(msg4, unsafe_allow_html=True) 
              #         st.markdown(msg5, unsafe_allow_html=True)
   
# #****************************************************************************************************************
            # if  classif_options == 'From Images' and models_img_options == 'InceptionV3':
              # if  source_options == 'Sample from training dataset (Random Choice)':
                  
              #     if st.button('Get an example and Classify'): 

              #       design, descrip, im_name, text_cleaned, row_index = demo_inputs.get_random_row()
                
              #       image = Image.open(demo_inputs.images_dir + im_name)
              #       st.image(image, channels="BGR",width=299,caption= im_name)

              #       image = demo_inputs.prepare_image(image, target=(299, 299))
                    
              #       pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_inception(image)
              #       prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
              #       col1, col2 = st.columns(2)

              #       with col1: 
              #         msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #         msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                    
              #         precision = np.amax(y_pred_proba)
              #         precision = precision * 100
              #         precision = np.round(precision,2)
                    
              #         msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #         st.markdown(msg1, unsafe_allow_html=True)
              #         st.markdown(msg2, unsafe_allow_html=True) 
              #         st.markdown(msg3, unsafe_allow_html=True) 
                                  
              #       with col2:                       
              #         msg4 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
              #         msg5 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
              #         st.markdown(msg4, unsafe_allow_html=True) 
              #         st.markdown(msg5, unsafe_allow_html=True)
     
##************************************************************************************************************************  
#                                                 # Bimodal (Text + Image)
##************************************************************************************************************************            
            # if  classif_options == 'From Text and Images (Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & Xception':
              # if  source_options == 'Sample from training dataset (Random Choice)':
            
              #     if st.button('Get an example and Classify'): 
                   
              #       design, descrip, im_name, text_cleaned,row_index= demo_inputs.get_random_row()
           
              #       st.text_input('Designation', design, disabled = True)
              #       st.text_input('Description', descrip, disabled = True)
                    
              #       image = Image.open(demo_inputs.images_dir + im_name)
              #       st.image(image, channels="BGR",width=299,caption= im_name)

              #       image = demo_inputs.prepare_image(image, target=(299, 299))

              #       pred_class ,pred_label, y_pred_proba = demo_inputs.predict_conv1D_simp_DNN_xception(text_cleaned, image)
              #       prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
              #       pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(text_cleaned) 
              #       pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(text_cleaned) 
              #       pred_class_Xcep ,pred_label_Xcep,y_pred_proba_Xcep = demo_inputs.predict_with_xception(image) 
                  
              #       col1, col2, col3 = st.columns(3)

              #       with col1: 
              #        msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #        msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                  
              #        precision = np.amax(y_pred_proba)
              #        precision = precision * 100
              #        precision = np.round(precision,2)
                  
              #        msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #        st.markdown(msg1, unsafe_allow_html=True)
              #        st.markdown(msg2, unsafe_allow_html=True) 
              #        st.markdown(msg3, unsafe_allow_html=True) 
                     
              #        with col2:                       
              #         msg4 = '<span style="color:black">Predicted product class and category from Text using Conv1D model: ' + str(pred_class_conv1) + ', ' + pred_label_conv1 + '</span>'
              #         st.markdown(msg4, unsafe_allow_html=True)

              #         msg6 = '<span style="color:black">Predicted product class and category from Text using Simple DNN model: ' + str(pred_class_sDNN) + ', ' + pred_label_sDNN + '</span>'
              #         st.markdown(msg6, unsafe_allow_html=True)

              #         msg8 = '<span style="color:black">Predicted product class and category from Image using Xception (CNN) model: ' + str(pred_class_Xcep) + ', ' + pred_label_Xcep + '</span>'
              #         st.markdown(msg8, unsafe_allow_html=True)
 
                      
              #       with col3:                       
              #          msg10 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
              #          msg11 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
              #          st.markdown(msg10, unsafe_allow_html=True) 
              #          st.markdown(msg11, unsafe_allow_html=True)
                          
##**********************************************************************************************************************            
            # if  classif_options == 'From Text and Images (Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & InceptionV3':
              # if  source_options == 'Sample from training dataset (Random Choice)':
                   
              #     if st.button('Get an example and Classify'): 
                   
              #       design, descrip, im_name, text_cleaned,row_index= demo_inputs.get_random_row()
                  
              #       st.text_input('Designation', design, disabled = True)
              #       st.text_input('Description', descrip, disabled = True)
                    
              #       image = Image.open(demo_inputs.images_dir + im_name)
              #       st.image(image, channels="BGR",width=299,caption= im_name)

              #       image = demo_inputs.prepare_image(image, target=(299, 299))
                    
              #       pred_class ,pred_label, y_pred_proba = demo_inputs.predict_conv1D_simp_DNN_inception(text_cleaned, image)
              #       prodcode, label = demo_inputs.get_real_class_info(row_index)
                    
              #       pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(text_cleaned) 
              #       pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(text_cleaned) 
              #       pred_class_incep ,pred_label_incep,y_pred_proba_incep = demo_inputs.predict_with_inception(image)
                    
              #       col1, col2, col3 = st.columns(3)

              #       with col1: 
              #        msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
              #        msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                  
              #        precision = np.amax(y_pred_proba)
              #        precision = precision * 100
              #        precision = np.round(precision,2)
                  
              #        msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
              #        st.markdown(msg1, unsafe_allow_html=True)
              #        st.markdown(msg2, unsafe_allow_html=True) 
              #        st.markdown(msg3, unsafe_allow_html=True) 
                     
              #        with col2:                       
              #         msg4 = '<span style="color:black">Predicted product class and category from Text using the Conv1D model: ' + str(pred_class_conv1) + ', ' + pred_label_conv1 + '</span>'
              #         st.markdown(msg4, unsafe_allow_html=True)

              #         msg6 = '<span style="color:black">Predicted product class and category from Text using the Simple DNN model: ' + str(pred_class_sDNN) + ', ' + pred_label_sDNN + '</span>'
              #         st.markdown(msg6, unsafe_allow_html=True)

              #         msg8 = '<span style="color:black">Predicted product class and category from Image using the InceptionV3 (CNN) model: ' + str(pred_class_incep) + ', ' + pred_label_incep + '</span>'
              #         st.markdown(msg8, unsafe_allow_html=True)

                    
                      
                    # with col3:                       
                    #    msg10 = '<span style="color:green">Actual product class : '  + str(prodcode) + '</span>'
                    #    msg11 = '<span style="color:green">Actual product category : ' + str(label) + '</span>'
                    #    st.markdown(msg10, unsafe_allow_html=True) 
                    #    st.markdown(msg11, unsafe_allow_html=True)
                  
##**************************************************************************************************************************** 
##----------------------------------------------Manual Input------------------------------------------------------------------------
##****************************************************************************************************************************            
            if  classif_options == 'From Text' and models_txt_options == 'Conv1D' :
              # if  source_options == 'Manual':
                  
                  user_Desig_input = st.text_area('Designation (required)', )
                  user_Descrip_input = st.text_area('Description (optional)', )

                  if st.button('Classify'): 
                     
                      if user_Desig_input == "" or user_Desig_input.isspace():              
                          st.write('Please enter the "Designation" field' ) 

                      else : 
                        try:
                            df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input)
                            df_cleaned = cleaning_text.CreateTextANDcleaning(df)                        
            
                            pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_conv1D(df_cleaned)                    
                    
                            precision = np.amax(y_pred_proba)
                            precision = precision * 100
                            precision = np.round(precision,2)
                          
                            msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                            msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                            msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
                            
                            st.markdown(msg1, unsafe_allow_html=True)
                            st.markdown(msg2, unsafe_allow_html=True)
                            st.markdown(msg3, unsafe_allow_html=True) 

                        except Exception as e:
                            msgError = '<span style="color:red">The provided text information is not valid</span>'
                            st.markdown(msgError, unsafe_allow_html=True)
                         
##**************************************************************************************************************** 
##****************************************************************************************************************           
            if  classif_options == 'From Text' and models_txt_options == 'Simple DNN' :
              # if  source_options == 'Manual':
                  
                  user_Desig_input = st.text_area('Designation (required)', )
                  user_Descrip_input = st.text_area('Description (optional)', )

                  if st.button('Classify'): 
                     
                      if user_Desig_input == "" or user_Desig_input.isspace(): 
                          st.write('Please enter the "Designation" field' ) 
                        
                      else :
                        try:  
                            df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input)  
                            df_cleaned = cleaning_text.CreateTextANDcleaning(df)                        
                            
                            pred_class , pred_label ,y_pred_proba =  demo_inputs.predict_with_simpDNN(df_cleaned)
                            
                            precision = np.amax(y_pred_proba)
                            precision = precision * 100
                            precision = np.round(precision,2)
                            
                            msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                            msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                            msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
                            st.markdown(msg1, unsafe_allow_html=True)
                            st.markdown(msg2, unsafe_allow_html=True)
                            st.markdown(msg3, unsafe_allow_html=True)

                        except Exception as e:
                            msgError = '<span style="color:red">The provided text information is not valid</span>'
                            st.markdown(msgError, unsafe_allow_html=True)
                

##**************************************************************************************************************** 
##****************************************************************************************************************            
            if  classif_options == 'From Images' and models_img_options == 'Xception' :
              # if  source_options == 'Manual':
                      
                  uploaded_file = st.file_uploader("Select an image file")

                  if st.button('Classify'): 

                    if uploaded_file is  None:
                      st.write('Please upload an image')  

                    elif uploaded_file is not None:                                             
                      content =  uploaded_file.read()
                      
                      try: 
                          image = Image.open(BytesIO(content)).convert("RGB")
                          st.image(image, channels="BGR",width=299) 

                          image = demo_inputs.prepare_image(image, target=(299, 299))

                          pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_xception_manu(image)
                          
                          precision = np.amax(y_pred_proba)
                          precision = precision * 100
                          precision = np.round(precision,2)
                          
                          msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                          msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                          msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'

                          st.markdown(msg1, unsafe_allow_html=True)
                          st.markdown(msg2, unsafe_allow_html=True)
                          st.markdown(msg3, unsafe_allow_html=True)

                      except IOError:
                          msgError = '<span style="color:red">The provided file is not a valid image</span>'
                          st.markdown(msgError, unsafe_allow_html=True)

##****************************************************************************************************************
##****************************************************************************************************************            
            if  classif_options == 'From Images' and models_img_options == 'InceptionV3' :
              # if  source_options == 'Manual':

                  uploaded_file = st.file_uploader("Select an image file")

                  if st.button('Classify'): 

                    if uploaded_file is  None:
                      st.write('Please upload an image')  

                    elif uploaded_file is not None:                                             
                      content =  uploaded_file.read()
                      
                      try: 
                          image = Image.open(BytesIO(content)).convert("RGB")
                          st.image(image, channels="BGR",width=299) 

                          image = demo_inputs.prepare_image(image, target=(299, 299))

                          pred_class ,pred_label,y_pred_proba = demo_inputs.predict_with_inception_manu(image)
                          
                          precision = np.amax(y_pred_proba)
                          precision = precision * 100
                          precision = np.round(precision,2)
                          
                          msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                          msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'
                          msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'

                          st.markdown(msg1, unsafe_allow_html=True)
                          st.markdown(msg2, unsafe_allow_html=True)
                          st.markdown(msg3, unsafe_allow_html=True)

                      except IOError:
                          msgError = '<span style="color:red">The provided file is not a valid image</span>'
                          st.markdown(msgError, unsafe_allow_html=True)                 

##****************************************************************************************************************
##****************************************************************************************************************            
            if  classif_options == 'From Text and Images (Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & Xception' :
              # if  source_options == 'Manual':
                                         
                       user_Desig_input = st.text_area('Designation (required)', )
                       user_Descrip_input = st.text_area('Description (optional)', )                      
                       uploaded_file = st.file_uploader("Select an image file")  

                                                   
                       if st.button('Classify'):
              
                         if (user_Desig_input == "" or user_Desig_input.isspace()) and uploaded_file is None:
                            st.write('Please enter the "Designation" field and upload an image' ) 
                          
                         elif uploaded_file is  None:
                             st.write('Please upload an image')
                                      
                         elif user_Desig_input == "" or user_Desig_input.isspace():                           
                                 st.write('Please enter the "Designation" field')
                             
                         else :
                             try:  
                               content =  uploaded_file.read()                       
                               image = Image.open(BytesIO(content)).convert("RGB")
                               st.image(image, channels="BGR",width=299)               
                               image = demo_inputs.prepare_image(image, target=(299, 299))

                             except IOError:                          
                                msgError = '<span style="color:red">The provided file is not a valid image</span>'
                                st.markdown(msgError, unsafe_allow_html=True)
                                #pass 
                             else:
                              try: 
                                  df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input) 
                                  df_cleaned = cleaning_text.CreateTextANDcleaning(df)   
                              except Exception as e:
                                msgError = '<span style="color:red">The provided text information is not valid</span>'
                                st.markdown(msgError, unsafe_allow_html=True)

                              else:
                                pred_class ,pred_label, proba = demo_inputs.predict_conv1D_simp_DNN_xception_manu(df_cleaned, image)                                                               
                                pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(df_cleaned) 
                                pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(df_cleaned) 
                                pred_class_Xcep ,pred_label_Xcep,y_pred_proba_Xcep = demo_inputs.predict_with_xception_manu(image) 
                                
                                col1, col2= st.columns(2)
                                
                                with col1: 
                                  msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                                  msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'  
                                  
                                  precision = np.amax(proba)
                                  precision = precision * 100
                                  precision = np.round(precision,2)
                                  
                                  msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
                                  st.markdown(msg1, unsafe_allow_html=True)
                                  st.markdown(msg2, unsafe_allow_html=True)
                                  st.markdown(msg3, unsafe_allow_html=True)
                                                                    
                                with col2: 
                                  msg4 = '<span style="color:black">Predicted product class and category from Text using the Conv1D model: ' + str(pred_class_conv1) + ', ' + pred_label_conv1 + '</span>'
                                  st.markdown(msg4, unsafe_allow_html=True)

                                  msg6 = '<span style="color:black">Predicted product class and category from Text using the Simple DNN model: ' + str(pred_class_sDNN) + ', ' + pred_label_sDNN + '</span>'
                                  st.markdown(msg6, unsafe_allow_html=True)

                                  msg7 = '<span style="color:black">Predicted product class and category from Image using the Xception (CNN) model: ' + str(pred_class_Xcep) + ', ' + pred_label_Xcep + '</span>'
                                  st.markdown(msg7, unsafe_allow_html=True)


                       
##****************************************************************************************************************            
            if  classif_options == 'From Text and Images (Bimodal)' and models_bimod_options == 'Conv1D & Simple DNN & InceptionV3' :
              # if  source_options == 'Manual':

                       user_Desig_input = st.text_area('Designation (required)', )
                       user_Descrip_input = st.text_area('Description (optional)', )                      
                       uploaded_file = st.file_uploader("Select an image file")  

                       if st.button('Classify'):
              
                         if (user_Desig_input == "" or user_Desig_input.isspace()) and uploaded_file is None:
                            st.write('Please enter the "Designation" field and upload an image' ) 
                          
                         elif uploaded_file is  None:
                             st.write('Please upload an image')
                                      
                         elif user_Desig_input == "" or user_Desig_input.isspace():                           
                                 st.write('Please enter the "Designation" field')
                             
                         else :
                             try:
                               content =  uploaded_file.read()                         
                               image = Image.open(BytesIO(content)).convert("RGB")
                               st.image(image, channels="BGR",width=299)               
                               image = demo_inputs.prepare_image(image, target=(299, 299))

                             except IOError:                          
                                msgError = '<span style="color:red">The provided file is not a valid image</span>'
                                st.markdown(msgError, unsafe_allow_html=True)
                                #pass 
                             else:
                              try: 
                                  df = cleaning_text.createdfManuel(user_Desig_input, user_Descrip_input) 
                                  df_cleaned = cleaning_text.CreateTextANDcleaning(df)   
                              except Exception as e:
                                msgError = '<span style="color:red">The provided text information is not valid</span>'
                                st.markdown(msgError, unsafe_allow_html=True)

                              else:
                                pred_class ,pred_label, proba = demo_inputs.predict_conv1D_simp_DNN_inception_manu(df_cleaned, image)                                                               
                                pred_class_conv1 , pred_label_conv1 ,y_pred_proba_conv1 =  demo_inputs.predict_with_conv1D(df_cleaned) 
                                pred_class_sDNN , pred_label_sDNN ,y_pred_proba_sDNN =  demo_inputs.predict_with_simpDNN(df_cleaned) 
                                pred_class_Xcep ,pred_label_Xcep,y_pred_proba_Xcep = demo_inputs.predict_with_inception_manu(image) 
                                
                                col1, col2= st.columns(2)
                                
                                with col1: 
                                  msg1 = '<span style="color:blue">Predicted product class : '  + str(pred_class) + '</span>'
                                  msg2 = '<span style="color:blue">Predicted category : ' + pred_label + '</span>'  
                                  
                                  precision = np.amax(proba)
                                  precision = precision * 100
                                  precision = np.round(precision,2)
                                  
                                  msg3 = '<span style="color:blue">Confidence : ' + str(precision) +'%'+ '</span>'
                                  st.markdown(msg1, unsafe_allow_html=True)
                                  st.markdown(msg2, unsafe_allow_html=True)
                                  st.markdown(msg3, unsafe_allow_html=True)
                                                                    
                                with col2: 
                                  msg4 = '<span style="color:black">Predicted product class and category from Text using the Conv1D model: ' + str(pred_class_conv1) + ', ' + pred_label_conv1 + '</span>'
                                  st.markdown(msg4, unsafe_allow_html=True)

                                  msg6 = '<span style="color:black">Predicted product class and category from Text using the Simple DNN model: ' + str(pred_class_sDNN) + ', ' + pred_label_sDNN + '</span>'
                                  st.markdown(msg6, unsafe_allow_html=True)

                                  msg7 = '<span style="color:black">Predicted product class and category from Image using the InceptionV3 (CNN) model: ' + str(pred_class_Xcep) + ', ' + pred_label_Xcep + '</span>'
                                  st.markdown(msg7, unsafe_allow_html=True)

