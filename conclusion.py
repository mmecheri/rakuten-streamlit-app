
import streamlit as st


def app():

    st.title("Conclusion and Possible Enhancements")
    body_page(text_page ='./page_descriptions/conclusion_txt.md')
def body_page(text_page):
    
    '''The text page. Read from .md file '''
    with open(text_page, 'r', encoding='utf-8') as txtpage: 
        txtpage = txtpage.read().split('---Insersetion---')
        
        st.markdown(txtpage[0], unsafe_allow_html=True) 
