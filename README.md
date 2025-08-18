# Military-Soldier-Safety-and-Weapon-Detection-using-YOLO-and-Computer-Vision

This project, "Military-Soldier-Safety-and-Weapon-Detection," uses a YOLOv8-based object detection model to identify military-related objects such as soldiers, weapons, vehicles, trenches, and civilians. The goal is to enhance situational awareness, safety monitoring, and threat detection through the application of computer vision.


# Model Prediction Showcase

This image showcases the model's ability to detect and classify various military objects in different scenarios. The bounding boxes indicate the detected objects, and the labels show the predicted class (e.g., "military_tank", "military_aircraft".....) along with the model's confidence score.

![val_batch0_pred](https://github.com/user-attachments/assets/18f65dcd-8228-46b1-9127-2bfb90c41198)

![val_batch1_pred](https://github.com/user-attachments/assets/d1853c70-5121-426a-ba1c-ea29b3346fa2)

![val_batch2_pred](https://github.com/user-attachments/assets/05824212-9a64-40a6-ad3d-fc26f9f1d754)


# Key Features

- Object Detection: A custom-trained YOLOv8 model that accurately identifies and classifies objects relevant to a military environment.

- Real-Time Processing: The model can perform real-time object detection on video feeds, allowing for immediate analysis.

- Threat Classification: Objects are categorized as threats (e.g., weapons, hostile soldiers) or non-threats (e.g., civilians).

- Interactive Web App: A user-friendly web interface built with Streamlit allows users to upload images or videos and visualize the detection results.

- Performance Evaluation: The model's effectiveness is measured using standard metrics like precision, recall, and mAP.

# Project Workflow

1. Data Collection and Preprocessing: A labeled dataset with YOLO annotations was gathered and preprocessed for compatibility with the model.

2. Model Training: A YOLO model was trained on the preprocessed data to detect and classify specific objects.

3. Real-Time Detection: The trained model is used to process video streams or static images, identifying objects in real time.

4. Deployment: The model is deployed as a web application using Streamlit, making it accessible and easy to use.

# Technologies Used

Category	            Technology

Language              Python

Deep Learning     	 YOLOv8

Libraries	          OpenCV, Streamlit, NumPy

Deployment	          Streamlit

# How to Run the App

Follow these steps to get the project up and running on your local machine.

1. Clone the repository:

   git clone https://github.com/JOTHILAKSHMI-H/Military-Soldier-Safety-and-Weapon-Detection-using-YOLO-and-Computer-Vision.git

   cd Military-Soldier-Safety-and-Weapon-Detection-using-YOLO-and-Computer-Vision

2. Install dependencies:

    - Ensure you have a Python environment set up.

    - Install the required libraries from the requirements.txt file.

       pip install -r requirements.txt

3. Place the trained model:

     Ensure your trained .pt or .h5 model file is in the correct directory as specified in the military.py script.

4. Run the Streamlit app:

    streamlit run military.py

  This command will launch the web application in your default browser.

