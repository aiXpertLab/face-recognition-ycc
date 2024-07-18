import os, PIL, random, streamlit as st
import numpy as np
import sklearn as sk
from sklearn import preprocessing
from sklearn.svm import SVC
import matplotlib.pyplot as plt

from mtcnn.mtcnn import MTCNN

def load_image(filename):
    image = PIL.Image.open(filename)
    image = image.convert('RGB')
    pixels = np.asarray(image)
    return pixels
    
def detect_image(pixels, required_size=(160, 160)):
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    # bug fix
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = PIL.Image.fromarray(face)
    image = image.resize(required_size)
    face_array = np.asarray(image)
    return face_array

def extract_face(filename, required_size=(160, 160)):
    pixels = load_image(filename)
    face_array = detect_image(pixels)
    return face_array

# load images and extract faces for all images in a directory
def load_faces(directory):
    faces = list()
    # enumerate files
    for filename in os.listdir(directory):
        # path
        path = directory + filename
        # get face
        face = extract_face(path)
        # store
        faces.append(face)
    return faces

# load a dataset that contains one subdir for each class that in turn contains images
def load_dataset(directory):
    X, y = list(), list()
    # enumerate folders, on per class
    for subdir in os.listdir(directory):
        # path
        path = directory + subdir + '/'
        # skip any files that might be in the dir
        if not os.path.isdir(path):
            continue
        # load all faces in the subdirectory
        faces = load_faces(path)
        # create labels
        labels = [subdir for _ in range(len(faces))]
        # summarize progress
        print('>loaded %d examples for class: %s' % (len(faces), subdir))
        # store
        X.extend(faces)
        y.extend(labels)
    return np.asarray(X), np.asarray(y)

# get the face embedding for one face
def get_embedding(model, face_pixels):
    # scale pixel values
    face_pixels = face_pixels.astype('float32')
    # standardize pixel values across channels (global)
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    # transform face into one sample
    samples = np.expand_dims(face_pixels, axis=0)
    # make prediction to get embedding
    yhat = model.predict(samples)
    return yhat[0]

def svc():
    # load faces
    data = np.load('5-celebrity-faces-dataset.npz')
    testX_faces = data['arr_2']
    # load face embeddings
    data = np.load('5-celebrity-faces-embeddings.npz')
    trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    # normalize input vectors
    in_encoder = preprocessing.Normalizer(norm='l2')
    trainX = in_encoder.transform(trainX)
    testX = in_encoder.transform(testX)
    # label encode targets
    out_encoder = preprocessing.LabelEncoder()
    out_encoder.fit(trainy)
    trainy = out_encoder.transform(trainy)
    testy = out_encoder.transform(testy)
    # fit model
    model = SVC(kernel='linear', probability=True)
    model.fit(trainX, trainy)
    # test model on a random example from the test dataset
    selection = random.choice([i for i in range(testX.shape[0])])
    random_face_pixels = testX_faces[selection]
    random_face_emb = testX[selection]
    random_face_class = testy[selection]
    random_face_name = out_encoder.inverse_transform([random_face_class])
    # prediction for the face
    samples = np.expand_dims(random_face_emb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)
    # get name
    class_index = yhat_class[0]
    class_probability = yhat_prob[0,class_index] * 100
    predict_names = out_encoder.inverse_transform(yhat_class)
    print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
    print('Expected: %s' % random_face_name[0])
    
    # plot for fun
    # pyplot.imshow(random_face_pixels)
    # title = '%s (%.3f)' % (predict_names[0], class_probability)
    # pyplot.title(title)
    # pyplot.show()
    
    fig, ax = plt.subplots()
    ax.imshow(random_face_pixels)
    title = '%s (%.3f)' % (predict_names[0], class_probability)
    ax.set_title(title)

    # Display the plot using Streamlit
    st.pyplot(fig)