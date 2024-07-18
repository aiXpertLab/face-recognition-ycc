import streamlit as st
from streamlit_extras.stateful_button import button
from utils import face_pipline as fp, streamlit_components
streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
t1,t2,t3,t4,t5,t6,t7 = st.tabs(["Extract Faces","Save Dataset","Embeddings","Face Classification","5","6MTCNN Detect","7Load Model"])
# -------------------------------------------------------------------------------------
import tensorflow as tf
from os import listdir
import matplotlib.pyplot as plt
import numpy as np

with t1: 
    if button("1. extract face", key="button1"):

        folder = './pages/data/train/ben_afflek/'
        i = 1
        cols = st.columns(7)
        # enumerate files
        for filename in listdir(folder):
            path = folder + filename
            face = fp.extract_a_face(path)
            print(i, face.shape)
            # plot
            with cols[(i - 1) % 7]:
                fig, ax = plt.subplots()
                ax.axis('off')
                ax.imshow(face)
                st.pyplot(fig)
            i += 1
            if i % 7 == 1:
                cols = st.columns(7)

with t2:
    if button("2.Save Datasize", key="button2"):
        trainX, trainy = fp.load_dataset('./pages/data/train/')
        print(trainX.shape, trainy.shape)
        # load test dataset
        testX, testy = fp.load_dataset('./pages/data/val/')
        # save arrays to one file in compressed format
        np.savez_compressed('5-celebrity-faces-dataset.npz', trainX, trainy, testX, testy)

with t3:
    if button("embeddings", key="button3"):
        data = np.load('5-celebrity-faces-dataset.npz')
        trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
        st.write('Loaded: ', trainX.shape, trainy.shape, testX.shape, testy.shape)
        model = tf.keras.models.load_model('./models/facenet_keras_2024.h5')
        # convert each face in the train set to an embedding
        newTrainX = list()
        for face_pixels in trainX:
            embedding = fp.get_embedding(model, face_pixels)
            newTrainX.append(embedding)
        newTrainX = np.asarray(newTrainX)
        print(newTrainX.shape)
        # convert each face in the test set to an embedding
        newTestX = list()
        for face_pixels in testX:
            embedding = fp.get_embedding(model, face_pixels)
            newTestX.append(embedding)
        newTestX = np.asarray(newTestX)
        print(newTestX.shape)
        # save arrays to one file in compressed format
        np.savez_compressed('5-celebrity-faces-embeddings.npz', newTrainX, trainy, newTestX, testy)
        
with t4:
    if button("SVM", key="button4"): fp.svc()
        