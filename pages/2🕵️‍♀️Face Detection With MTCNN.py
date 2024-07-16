import streamlit as st
from utils import streamlit_components
streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
# -------------------------------------------------------------------------------------
from matplotlib import pyplot
import tensorflow as tf
from mtcnn.mtcnn import MTCNN
from app.draw_boxes import draw_image_with_boxes
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

filename = './pages/img/y2.jpg'


pixels = pyplot.imread(filename)# load the photograph
detector = MTCNN()

faces = detector.detect_faces(pixels)

draw_image_with_boxes(filename=filename, result_list=faces)