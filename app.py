import streamlit as st
import cv2
import numpy as np
from PIL import Image
from PIL.ImageOps import grayscale

st.set_page_config(page_title="Image processing app", page_icon=":camera:", layout="wide")
st.title("Smart Photo Editor")
st.write("Завантажте фото та застосуйте на нього інтелектуальні фільтри!")
st.sidebar.header("Налаштування Фільтрів")

uploaded_file = st.file_uploader("06еріть фото...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Орігінальне Фото")
        st.image(img_array, use_container_width=True)
    filter_option = st.sidebar.selectbox("Оберіть ефект:", ["оригінал", "Чорно-білий", "Збільшити яскравість", "розмиття", "контраст", "інверсія кольорів", "Ефект олівця"])
    processing_img = img_array.copy()

    if filter_option == "Чорно-білий":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processing_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    if filter_option == "Збільшити яскравість":
        processing_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)
    if filter_option == "розмиття":
        processing_img = cv2.GaussianBlur(img_array, (15, 15), 0)
    if filter_option == "контраст":
        processing_img = cv2.convertScaleAbs(img_array,alpha=1.7, beta=0)
    if filter_option == "інверсія кольорів":
        processing_img = 255 - img_array
    if filter_option == "Ефект олівця":
        gray, color = cv2.pencilSketch(img_array, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
        processing_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)


    with col2:
        st.subheader("Оброблена фотографія")
        st.image(processing_img, use_container_width=True)