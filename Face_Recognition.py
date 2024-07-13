import streamlit as st

from utils import streamlit_components, streamlit_docs
streamlit_components.streamlit_ui('🐬🦣 Face Recognition 🍃🦭')
# ----------------------------------------------------------------------
t1,t2=st.tabs(['General','MTCNN'])
with t1: streamlit_docs.general()
with t2: streamlit_docs.MTCNN()
    
