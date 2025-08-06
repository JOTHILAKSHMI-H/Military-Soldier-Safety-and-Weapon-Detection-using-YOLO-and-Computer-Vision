import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile

# load YOLOv8 model
model = YOLO(r'E:\project\military_object_detection_final\Military_Soldier_Safety_and_Weapon_Detector_model3\weights\military_yolov8m.pt')


# Title
st.title('Military Soldier Safety and Weapon Detector')

# Select mode
mode = st.radio("Choose the input type:", ("Image", "Video"))

if mode == "Image":
    # upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        image_np = np.array(image)
        results = model.predict(image_np)
        result = results[0]
        rendered_image = result.plot()

        # Column layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        with col2:
            
            st.subheader("Detected Result")
            st.image(rendered_image, use_container_width=True)

elif mode == "Video":
    uploaded_video = st.file_uploader("🎞️ Upload a video", type=["mp4", "avi", "mov", "mkv"])
    if uploaded_video is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Predict
            results = model.predict(frame_rgb, conf=0.4)
            result = results[0]
            rendered_frame = result.plot()

            # Display
            stframe.image(rendered_frame, channels="RGB", use_container_width=True)

        cap.release()
        st.success("✅ Video processing complete.")