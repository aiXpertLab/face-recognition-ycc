import streamlit as st

from utils import streamlit_components, streamlit_docs
streamlit_components.streamlit_ui('🐬🦣 Face Recognition 🍃🦭')
# ----------------------------------------------------------------------
tab1, tab2 = st.tabs(["General","MTCNN",])

with tab1: streamlit_docs.general()
with tab2: streamlit_docs.MTCNN()
    
