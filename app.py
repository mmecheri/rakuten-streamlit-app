import streamlit as st
from multiapp import MultiApp
import home,  demo, dataset ,models, conclusion



# 🧠 Set up the Streamlit app config BEFORE anything else
st.set_page_config(
    page_title="Data Science Project: Product Categorization",
    page_icon="🔀",
    # page_icon='./doc/icon_app.png',
    
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={    
    'Report a bug': 'https://github.com/mmecheri/Data_Scientist_Rakuten_Project/issues',
    'About': '''
    # Rakuten Product Classification  
    A multimodal classification project using product text and image data.  
    Version: 1.0.0  
    Author: Mourad MECHERI  
    '''
}
)

def main():
    
    ##st.set_page_config('rakupy', layout="wide")  
    
    apps = MultiApp('Navigation', 'Menu') 
    ## Add all Applications     
    apps.add_app("Project Overview", home.app)
    apps.add_app("Dataset", dataset.app)
    apps.add_app("Modeling", models.app)
    apps.add_app("Demo", demo.app)
    apps.add_app("Conclusion", conclusion.app)

    # The main app
    apps.run()

if __name__ == '__main__': 
     main()
