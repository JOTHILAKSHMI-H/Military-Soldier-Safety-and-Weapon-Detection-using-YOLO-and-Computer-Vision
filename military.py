import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# load YOLOv8 model
model = YOLO(r'E:\project\final_project\military_best.pt')


# Title
st.title('Military Soldier Safety and Weapon Detector')

# upload image
uploaded_file = st.file_uploader('upload a image', type= ['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # load image with PIL
    image = Image.open(uploaded_file).convert("RGB")
    
    # display original image
    st.image(image, caption = "Uploaded Image", use_column_width= True)
    
    # convert PIL image to numpy array
    image_np = np.array(image)
    
    # run yolov8 prediction on the image
    results = model.predict(image_np)
    
    # extract first result and render bounding box
    result = results[0]
    rendered_image = result.plot() # numpy array with box drawn
    
    # Display result
    st.image(rendered_image, caption="Detected Image", use_column_width=True)