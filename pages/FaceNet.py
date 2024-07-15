import streamlit as st
from utils import streamlit_components
streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
# -------------------------------------------------------------------------------------
# model: https://drive.google.com/open?id=1pwQ3H4aJ8a6yyJHZkTwtjcL4wYWQb7bn

from keras.models import load_model
# load the model
model = load_model('./models/facenet_keras.h5')
# summarize input and output shape
print(model.inputs)
print(model.outputs)