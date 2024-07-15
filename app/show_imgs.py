import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

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
