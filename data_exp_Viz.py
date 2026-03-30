
import streamlit as st
from PIL import Image



def app():

    read_page_text(text_page ='./page_descriptions/data_exp_viz_txt.md')     

     
def read_page_text(text_page):
    
        
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col2:
             image = Image.open('./doc/Nas_values.png')
             st.image(image, use_column_width='auto')
            
            st.markdown(txtpage[1], unsafe_allow_html=True)
            col3, col4 = st.columns(2)
            with col4:
            #  image = Image.open('./doc/small_imgs_2_exp.png')
             st.image(image, use_column_width='auto')
            
            st.markdown(txtpage[2], unsafe_allow_html=True)
            
            #
            col5, col6 = st.columns([0.5,2])
            with col6:
             image = Image.open('./doc/resemblance_classe.png')
             st.image(image, use_column_width='auto')
            
            st.markdown(txtpage[3], unsafe_allow_html=True)   
            st.markdown(txtpage[6], unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                image1 = Image.open('./doc/classe_1180_WC.png')
                st.image(image1, use_column_width='auto')
            with col2:
              image2 = Image.open('./doc/classe_1180_imgs.png')
              st.image(image2, use_column_width='auto')
  
            col3, col4 = st.columns(2)
            with col3:
                image3 = Image.open('./doc/classe_2583_WC.png')
                st.image(image3, use_column_width='auto')
            with col4:
              image4 = Image.open('./doc/classe_2583_imgs.png')
              st.image(image4, use_column_width='auto')
              
            st.markdown(txtpage[7], unsafe_allow_html=True)
            # image5 = Image.open('./doc/categories.png')
            # st.image(image5, use_column_width='auto')
            with open('./doc/categories.md', 'r', encoding='utf-8') as f:
              markdown_content = f.read()
              st.markdown(markdown_content, unsafe_allow_html=True)

         # with col7:
            st.markdown(txtpage[4], unsafe_allow_html=True)       
            image = Image.open('./doc/repartition_classes_2.png')
            st.image(image, use_column_width='auto')
          #with col8:
            st.markdown(txtpage[5], unsafe_allow_html=True)
            agree1 = st.checkbox('Show more details')

            if agree1:
            #  image = Image.open('./doc/proportion_table.png')
            #  st.image(image, use_column_width='auto')
              with open('./doc/proportion_table.md', 'r', encoding='utf-8') as f:
               markdown_content = f.read()
               st.markdown(markdown_content, unsafe_allow_html=True)