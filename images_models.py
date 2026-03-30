import streamlit as st
from PIL import Image

  
def app():

    st.subheader("Image-based Modeling")
    page_content(text_page ='./page_descriptions/models_image_txt.md')     
                
       
def page_content(text_page):
        
        '''The text page. Read from .md file '''
        with open(text_page, 'r', encoding='utf-8') as txtpage: 
            txtpage = txtpage.read().split('---Insersetion---')
            st.markdown(txtpage[0], unsafe_allow_html=True)
           # Paramères ---------------------------------------------------------------------------------
            st.markdown(txtpage[1], unsafe_allow_html=True)
            col1, col2 = st.columns([0.3,1])

            with col2:           
                image1 = load_image('imgs_selected_models.png')
                st.image(image1, use_column_width='auto')
                      
            
            agree1 = st.checkbox('Show the parameters used')

            if agree1:       
             st.markdown(txtpage[2], unsafe_allow_html=True)

            agree2 = st.checkbox('Classification layers')

            if agree2:       
               image12 = load_image('classification_layers.png')
               st.image(image12, use_column_width='auto')

       # STEP1 Démarche--------------------------------------------------------------------------------
            st.markdown(txtpage[3], unsafe_allow_html=True)
       # STEP1 Résultats--------------------------------------------------------------------------------
    
            st.markdown(txtpage[4], unsafe_allow_html=True)
            image3 = load_image('result_img_step1.png')
            st.image(image3, use_column_width='auto')
            
            st.markdown(txtpage[5], unsafe_allow_html=True)
            image4 = load_image('result_img_step1_top_5.png')
            st.image(image4, use_column_width='auto')
            
            agree3 = st.checkbox('Show F1-scores by class, by category, and by model')

            if agree3:
              col1, col2, col3 = st.columns([6,0.2, 1])     
            #   image5 = load_image('result_img_step1_top_5_details.png')
            #   st.image(image5, use_column_width='auto')
              with col1:
                with open("./doc/result_img_step1_top_5_details.md", "r", encoding="utf-8") as f:
                    md_content = f.read()
                    st.markdown(md_content, unsafe_allow_html=True)
              with col3:
                st.markdown("⚠️ indicates that the weighted F1-score is below the image baseline threshold (0.55), which may require further model improvement.")



            st.markdown('----------' )      
      # STEP2 Démarche--------------------------------------------------------------------------------
       # STEP2 Résultats---------------------------------------------------------------------------------       
            col3, col4 = st.columns([0.75,0.25])
            with col3:
              st.markdown(txtpage[6], unsafe_allow_html=True) 
              image6 =  load_image('result_img_step2.png')
              st.image(image6, use_column_width='auto')
              st.info("""Data augmentation does not seem to improve performance, and may even slightly reduce it.  
              However, it might help the model generalize better on new datasets.""")

            with col4:
              st.markdown(txtpage[15], unsafe_allow_html=True) 
            
            st.markdown('----------' ) 
            
            col4, col5 = st.columns([0.75,0.25])
           
            with col4:
       # STEP3 Démarche--------------------------------------------------------------------------------
             st.markdown(txtpage[7], unsafe_allow_html=True)                 
       # STEP3 Résultats--------------------------------------------------------------------------------- 
             image7 =  load_image('result_img_step3.png')
             st.image(image7, use_column_width='auto')
             st.info('''   
              We observe performance improvements for all models, except for DenseNet121 which stayed the same.  
              Xception now ranks first with a weighted F1-score of 0.65, showing a 4% improvement compared to its score in Step 1.''' )

             st.markdown('----------' ) 
            with col5:
             st.markdown(txtpage[16], unsafe_allow_html=True)
        # STEP4 Démarche--------------------------------------------------------------------------------
            st.markdown(txtpage[8], unsafe_allow_html=True)
   # # # STEP4 Résultats---------------------------------------------------------------------------------
            image8 =  load_image('result_LR_step4.png')
            st.image(image8,use_column_width='auto')           
            agree4 = st.checkbox("Show an example of the method used to find the optimal learning rates (Xception)")

            if agree4:
                col1, col2 = st.columns([2,1])        
                with col1:
                    image9 =  load_image('exemple_LR_Xception.png')
                    st.image(image9, use_column_width='auto')
                with col2:
                      st.markdown(txtpage[9], unsafe_allow_html=True)
                    
                col3, col4 = st.columns([2,1]) 
                with col3:
                    image10 =  load_image('exemple_LR_Xception_Vs_Loss.png')
                    st.image(image10, use_column_width='auto')
                with col4:
                    st.markdown(txtpage[10], unsafe_allow_html=True)
            st.markdown('----------' ) 
        # STEP5 Démarche--------------------------------------------------------------------------------
            col6, col7 = st.columns([0.75,0.25])
            with col6:
             st.markdown(txtpage[11], unsafe_allow_html=True)
    #     # STEP5 Résultats---------------------------------------------------------------------------------
             st.markdown(txtpage[12], unsafe_allow_html=True)
             image11 =  load_image('result_img_step5.png')
             st.image(image11, use_column_width='auto')
            with col7:
             st.markdown(txtpage[17], unsafe_allow_html=True)
    
            st.info(txtpage[13])
    
            st.markdown('----------' ) 
            st.info(txtpage[14])


@st.cache_resource()
def load_image(imageName):
    image = Image.open('./doc/'+imageName)
    return image