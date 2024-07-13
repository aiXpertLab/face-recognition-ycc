import streamlit as st
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle
from mtcnn.mtcnn import MTCNN

def draw_image_with_boxes(filename, result_list):

    # Read the image
    data = plt.imread(filename)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Display the image
    ax.imshow(data)
    
    # Plot each box
    for result in result_list:
        # Get coordinates
        x, y, width, height = result['box']
        # Create the shape
        rect = Rectangle((x, y), width, height, fill=False, color='red')
        # Draw the box
        ax.add_patch(rect)
        for _, value in result['keypoints'].items():
            # create and draw dot
            dot = Circle(value, radius=2, color='red')
            ax.add_patch(dot)
    
    # Display the plot in Streamlit
    st.pyplot(fig)

