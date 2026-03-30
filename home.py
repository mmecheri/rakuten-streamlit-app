import streamlit as st

     
# homme.py

def app():
    
    st.title("Rakuten France Multimodal Product Data Classification")
    
    st.header("The project") 
    # Projet Overview 1
    page_content(text_page ='./page_descriptions/description_projet.md')  
    
    
def page_content(text_page):
        
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
        st.markdown('----------' ) 
        st.markdown(txtpage[1], unsafe_allow_html=True)
       
       