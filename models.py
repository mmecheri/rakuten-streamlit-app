
import streamlit as st
import text_models,images_models, bimodal
from submultiapp import SubMultiApp


def app():
    
    st.title("Modeling")
    
    apps = SubMultiApp(None, 'Modeling')
    #
    apps.add_app("Text", text_models.app)
    apps.add_app("Images", images_models.app)
    apps.add_app("Bimodal", bimodal.app)
    
    apps.run()