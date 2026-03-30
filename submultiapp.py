"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st



class SubMultiApp:

 
    def __init__(self, bar_header=None, radio_label= None):
        self.apps = []
        self.bar_header = bar_header
        self.radio_label = radio_label
        
                 

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({"title": title, "function": func})
# @st.cache
    def run(self):
        app_state = st.experimental_get_query_params()
        app_state = {
            #k: v[0] if isinstance(v, list) else v for k, v in list(app_state.items())
        }  # fetch the first item in each query string as we don't have multiple values for each query string key in this example


        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(app_state["page"]) if "page" in app_state else 0

        if self.bar_header != None:
         st.sidebar.header(self.bar_header)

        if self.radio_label == None:
         self.radio_label ='Menu'
         
         
        title = st.sidebar.radio(self.radio_label, titles, index=default_radio, key="radio")
        
        st.experimental_set_query_params(**st.session_state.to_dict())
        functions[titles.index(title)]()
        
