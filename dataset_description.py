import streamlit as st
import pandas as pd
import numpy as np
import data_exp_Viz, data_preprocessing
from multiapp import MultiApp
from PIL import Image

def app():

    st.subheader('Data description')
  
    read_page_text(text_page ='./page_descriptions/data_description_txt.md')     
  
    load_samples()
#

def read_page_text(text_page):
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('------')
            st.markdown(txtpage[0], unsafe_allow_html=True)


def load_samples():
    
    col1, col2, col3 = st.columns([2.5,1,0.75])

    with col1:
        st.markdown('Training Dataset Preview (X_train):',  unsafe_allow_html=True) 
        df = pd.read_pickle('./demo_Inputs/data/X_train_simulated_product_examples.pkl')  
        st.dataframe(df.set_index('Id'), use_container_width=True)   
        # st.dataframe(df) 
        # print(df)
        agree1 = st.checkbox('Display columns descriptions')
        if agree1:
              with open('./page_descriptions/data_col_description.md', 'r', encoding='utf-8') as subpage1: 
               subpage1 = subpage1.read().split('------')
               st.markdown(subpage1[0], unsafe_allow_html=True)
    
    with col2:
           st.markdown('Classes associated with «**prdtypecode**»(y_train)',  unsafe_allow_html=True) 
        #    df = pd.read_pickle('./demo_Inputs/data/Extract_Ytrain_demo_FINAL.pkl')  
           df = pd.read_pickle('./demo_Inputs/data/y_train_simulated_prdtypecode_examples.pkl')              
           df.index.name = 'Id' 
           # print(df)    
           # st.dataframe(df) 
           st.dataframe(df.set_index('Id')) 
    
    
    with col3:
        with open('./page_descriptions/data_img_description.md', 'r', encoding='utf-8') as subpage2: 
            subpage2 = subpage2.read().split('------')
            st.markdown(subpage2[0], unsafe_allow_html=True) 
         
    # image = Image.open('./doc/exmpl_data_with_image.png')
    image = Image.open('./doc/simulated_data_example_display.png')
    st.image(image,output_format="auto")  
       
