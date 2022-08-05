import Homepage as Homepage
import Deployment.Data_Visualization as Data_Visualization
import Analysis
import streamlit as st

st.set_page_config(
    page_title="Google Ads Political",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://discuss.streamlit.io/',
        'Report a bug': "https://github.com/streamlit/streamlit/issues/new/choose",
        'About': ""
    }
)

PAGES = {'Homepage': Homepage,
         'Data Visualization': Data_Visualization,
         'Analysis': Analysis}

st.sidebar.title ('Menu')
selected = st.sidebar.selectbox ('Select Page: ', ['Homepage', 'Data Visualization', 'Analysis'])

page = PAGES [selected]

page.app ()
