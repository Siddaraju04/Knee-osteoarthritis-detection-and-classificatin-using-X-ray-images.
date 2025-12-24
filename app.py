import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps

import base64
import streamlit as st

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:background/background.avif;base64,%s");
    background-position: center;
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('background/1.png')

def import_and_predict(image_data, model):
    
        size = (75,75)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        image = (image.astype(np.float32) / 255.0)

        img_reshape = image[np.newaxis,...]

        prediction = model.predict(img_reshape)
        
        return prediction

model = tf.keras.models.load_model('model.h5')

st.write("""
         # Knee Osteoarthritis Detection and Classification Using X-Rays
         """
         )

st.write("Knee Osteoarthritis Detection and Classification Using X-Rays")

file = st.file_uploader("upload an image file", type=["jpg", "png"])
#
if file is None:
    st.text("please select a image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("It is a Normal!")
    else:
        st.write("It is a Osteoarthritis!")
    
    