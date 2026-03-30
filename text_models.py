import streamlit as st
from PIL import Image
#   
def app():

    st.subheader("Text Modeling")
    read_page_text(text_page ='./page_descriptions/models_text_txt.md')     
                
  
     
def read_page_text(text_page):
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
            
            image1 = load_image('tab_ml_text.png')
            st.image(image1, use_column_width='auto')
            
            agree1 = st.checkbox('Show the ML parameters used')

            if agree1:                          
                image2 = load_image('tab_ml_text_parem.png')
                st.image(image2, use_column_width='auto')
                
                
            st.markdown(txtpage[1], unsafe_allow_html=True)
            image3 = load_image('tab_dl_text.png')
            st.image(image3, use_column_width='auto')
            
            agree2 = st.checkbox('Show the DL parameters used')

            if agree2:
              st.markdown(txtpage[2], unsafe_allow_html=True)  
            
            agree3 = st.checkbox('Show detailed class-wise results for Conv1D and Simple DNN (Weighted F1-score)')

            if agree3: 
              # image4 =  load_image('tab_dl_details_conv1d_simpleDNN.png')
              # st.image(image4, use_column_width='auto')
              with open("./doc/tab_dl_details_conv1d_simpleDNN.md", "r", encoding="utf-8") as f:
                md_content = f.read()
              st.markdown(md_content, unsafe_allow_html=True)
              
            agree4 = st.checkbox("Show the least accurate classes (F1-score lower than the baseline model's score of 0.80)")
            
            if agree4: 
               col1, col2 = st.columns([2,1])        
               with col1:
                  #  image5 = load_image('conv1_simpleDNN_less_ref.png')
                  #  st.image(image5, use_column_width='auto')
                  with open("./doc/conv1_simpleDNN_less_ref.md", "r", encoding="utf-8") as f:
                   md_content = f.read()
                   st.markdown(md_content, unsafe_allow_html=True)
               with col2:
                    st.markdown(txtpage[3], unsafe_allow_html=True)
                    
            st.info(txtpage[4])
           

@st.cache_resource()
def load_image(imageName):
      image = Image.open('./doc/'+imageName)
      return image  
    