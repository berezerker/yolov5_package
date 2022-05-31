import streamlit as st
import os
import sys
import cv2
from PIL import Image, ImageDraw
sys.path.append('../')
from yolov5_hse.demo import detect_for_web_demo

root_dir = os.path.dirname(__file__)
weights = root_dir + "/model_float16_quant.tflite"
class_names = root_dir + "/class_names.txt"

def main():
    st.header("Yolov5 web demo")
    st.write("Upload your image for detecting:")

    uploaded_file = st.file_uploader("Choose an image...")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, "your image")
        resulting_image = detect_for_web_demo(weights, img, 416, 0.25, 0.45, class_names)
        st.image(resulting_image, "resulting image after detecting")
        
if __name__ == "__main__":
    main()
    
