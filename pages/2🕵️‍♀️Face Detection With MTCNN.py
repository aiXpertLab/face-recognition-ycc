import streamlit as st
from utils import streamlit_components
streamlit_components.streamlit_ui('🦣 Face Detection With MTCNN')
# -------------------------------------------------------------------------------------
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from app.draw_boxes import draw_image_with_boxes

filename = './images/m2.jpg'

pixels = pyplot.imread(filename)# load the photograph
detector = MTCNN()

faces = detector.detect_faces(pixels)

draw_image_with_boxes(filename=filename, result_list=faces)