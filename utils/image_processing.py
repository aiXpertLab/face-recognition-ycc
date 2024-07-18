import streamlit as st
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
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


def show_img(imgs: list, img_names: list) -> None:
    fig, axs = plt.subplots(1, len(imgs), figsize=(5*len(imgs), 5))
    
    if len(imgs) == 1:
        axs = [axs]
    
    for i, (img, name) in enumerate(zip(imgs, img_names)):
        axs[i].imshow(img)
        axs[i].set_title(name)
        axs[i].set_xticks([])
        axs[i].set_yticks([])
    
    plt.tight_layout(h_pad=3)
    st.pyplot(fig)
