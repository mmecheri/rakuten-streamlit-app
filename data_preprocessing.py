
import streamlit as st
from PIL import Image



#   
def app():

    st.subheader("Data preprocessing")
    read_page_text(text_page ='./page_descriptions/data_preprocessing_txt.md')     
                
  
     
def read_page_text(text_page):
        '''The text page. Read from .md file '''
        
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)

           