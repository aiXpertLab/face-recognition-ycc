import streamlit as st, os
import matplotlib

import utils.face_pipline as fp

def draw_image_with_boxes(filename, result_list):

    # Read the image
    data = matplotlib.pyplot.imread(filename)
    
    # Create a figure and axis
    fig, ax = matplotlib.pyplot.subplots()
    
    # Display the image
    ax.imshow(data)
    
    # Plot each box
    for result in result_list:
        # Get coordinates
        x, y, width, height = result['box']
        # Create the shape
        rect = matplotlib.patches.Rectangle((x, y), width, height, fill=False, color='red')
        # Draw the box
        ax.add_patch(rect)
        for _, value in result['keypoints'].items():
            # create and draw dot
            dot = matplotlib.patches.Circle(value, radius=2, color='red')
            ax.add_patch(dot)
    
    # Display the plot in Streamlit
    st.pyplot(fig)


def show_img(imgs: list, img_names: list) -> None:
    fig, axs = matplotlib.subplots(1, len(imgs), figsize=(5*len(imgs), 5))
    
    if len(imgs) == 1:
        axs = [axs]
    
    for i, (img, name) in enumerate(zip(imgs, img_names)):
        axs[i].imshow(img)
        axs[i].set_title(name)
        axs[i].set_xticks([])
        axs[i].set_yticks([])
    
    matplotlib.pyplot.tight_layout(h_pad=3)
    st.pyplot(fig)


def show_extracted_faces(folder):
    with st.spinner('extracting ...'):
        i = 1
        cols = st.columns(7)
        # enumerate files
        for filename in os.listdir(folder):
            path = folder + filename
            face = fp.extract_face(path)
            print(i, face.shape)
            # plot
            with cols[(i - 1) % 7]:
                fig, ax = matplotlib.pyplot.subplots()
                ax.axis('off')
                ax.imshow(face)
                st.pyplot(fig)
            i += 1
            if i % 7 == 1:
                cols = st.columns(7)
    st.success('done')