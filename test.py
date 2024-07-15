# import streamlit as st
# from utils import streamlit_components
# streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
# -------------------------------------------------------------------------------------
# example of creating a face embedding
from keras_vggface.vggface import VGGFace
# create a vggface2 model
model = VGGFace(model='resnet50')
# summarize input and output shape
print('Inputs: %s' % model.inputs)
print('Outputs: %s' % model.outputs)