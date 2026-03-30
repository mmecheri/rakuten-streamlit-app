import streamlit as st
from PIL import Image

def app():

    st.subheader("Modeling based on Text and Image data")
    read_page_text(text_page ='./page_descriptions/bimodal_txt.md')
                

    
def read_page_text(text_page):

            '''The text page. Read from .md file '''
            with open(text_page, 'r', encoding='utf-8') as txtpage: 
                txtpage = txtpage.read().split('---Insersetion---')
                st.markdown(txtpage[0], unsafe_allow_html=True)
                
                st.markdown(txtpage[1], unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(txtpage[2], unsafe_allow_html=True)
                with col2:
                     st.markdown(txtpage[3], unsafe_allow_html=True)
                     
                st.markdown(txtpage[4], unsafe_allow_html=True)    
                st.markdown(txtpage[5], unsafe_allow_html=True)
                
                agree1 = st.checkbox('Show the weights used for Weighted Average voting')
              
                if agree1:
                  st.markdown(txtpage[6], unsafe_allow_html=True)
                  
              # Résultats --------------------------Simple DNN conv1E Xception-----------------------------------------------
                st.markdown(txtpage[7], unsafe_allow_html=True)
                image1 = load_image('bimodal_result_1.png')               
                st.image(image1, use_column_width='auto')
              
                agree2 = st.checkbox('Show F1-scores by class and category using the first voting combination')
             
                if agree2:

                #   image2 = load_image('bimodal_avec_xception.png') 
                #   st.image(image2, use_column_width='auto')
                 with open("./doc/bimodal_avec_xception.md", "r", encoding="utf-8") as f:
                  md_content = f.read()
                  st.markdown(md_content, unsafe_allow_html=True)
                  
               # Résultats --------------------------Simple DNN conv1E Inception-----------------------------------------------
                st.markdown(txtpage[8], unsafe_allow_html=True)
                image3 = load_image('bimodal_result_2.png')               
                st.image(image3, use_column_width='auto')
                agree3 = st.checkbox('Show F1-scores by class and category using the second voting combination')
   
                if agree3:

                #    image4 = load_image('bimodal_avec_inceptionV3.PNG') 
                #    st.image(image4, use_column_width='auto')
                 with open("./doc/bimodal_avec_inceptionV3.md", "r", encoding="utf-8") as f:
                  md_content = f.read()
                  st.markdown(md_content, unsafe_allow_html=True)
 
                st.markdown(txtpage[9], unsafe_allow_html=True)
                agree4 = st.checkbox('Analyze and compare the results of the two voting combinations')


                if agree4:
                    # image5 = load_image('tableau_comparison_last.PNG') 
                    # st.image(image5, use_column_width='auto')
                    # with open("./doc/tableau_comparison_last.md", "r", encoding="utf-8") as f:
                    #  md_content = f.read()
                    #  st.markdown(md_content, unsafe_allow_html=True)              
                    st.subheader("Ensemble Model Comparison")

                    # col1, col2, col3 = st.columns([4, 1, 1])
                    col1, col2 = st.columns([4, 1])

                    with col1:
                        st.markdown("#### F1-Score Table")
                        with open("./doc/tableau_comparison_last.md", "r", encoding="utf-8") as f:
                            md_content = f.read()
                        st.markdown(md_content, unsafe_allow_html=True)

                    with col2:
                        st.markdown("##### Best with Xception")
                        st.markdown("""
                        - adult books  
                        - figurines and Toy Pop  
                        - Playing cards  
                        - toys for children  
                        - Remote controlled models  
                        - Early childhood
                        - Food              
                        - magazines  
                        - children books and magazines  
                        - Books  
                        - Online distribution of video games  
                        """)

                  
                        st.markdown("##### Best with InceptionV3")
                        st.markdown("""
                        - imported video games  
                        - video games accessories  
                        - Games and consoles  
                        - figurines, masks and role-playing games  
                        - board games  
                        - Accessories children  
                        - toys, outdoor playing, clothes  
                        - Interior furniture and bedding  
                        - games  
                        - furniture kitchen and garden 
                        - gardening and DIY  
                        """)

                        st.markdown("##### ❌ Labels where ensembling does **not** improve predictions:")
                        st.markdown("For these labels, neither ensemble (Conv1D, DNN, Xception or Conv1D, DNN, InceptionV3) outperformed the best single model (Conv1D, DNN simple, Xception, or Inception V3).")


                        st.markdown("""
                        - **figurines, masks and role-playing games**  
                        - **board games**  
                        - **Remote controlled models**  
                        - **Accessories children**  
                        - **Interior accessories**
                        - **Decoration interior**  
                        - **Supplies for domestic animals**  
                        - **stationery**  
                        - **Piscine spa**  
                        - **Online distribution of video games**
                        """)
            
                
                
                
                st.markdown('----------')
                st.info(txtpage[10])


#@st.cache_resource()
@st.cache_resource()
def load_image(imageName):
    #data = dict()
    image = Image.open('./doc/'+imageName)
    return image