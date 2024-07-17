import streamlit as st
from utils import streamlit_components
streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
# -------------------------------------------------------------------------------------
# #Step 1
# from utils import inception_resnet_v1

# #Step 2
# model = inception_resnet_v1.InceptionResNetV1()
# model.load_weights('./models/facenet_keras_weights.h5')

# model.save('./models/facenet_complete_model_leo.h5')

import tensorflow as tf

model = tf.keras.models.load_model('./models/facenet_complete_model_leo.h5')
# # model = tf.keras.models.load_model('./models/resnet51q_imagenet.h5')
# model = tf.keras.models.load_model('./models/GN_W1.3_S2_ArcFace_epoch48.h5')

# # model = FaceNet()

# # # summarize input and output shape
st.write(model.inputs)
st.write(model.outputs)

# import cv2
# st.write(cv2.__version__)