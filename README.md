# Military-Soldier-Safety-and-Weapon-Detection-using-YOLO-and-Computer-Vision

This project uses a YOLOv8-based object detection model to identify military-related objects, including soldiers, weapons, vehicles, trenches, and civilians. It aims to assist in situational awareness, safety monitoring, and threat detection using computer vision.

### Project Approach 
#### Data Collection & Preprocessing
Gathered a labeled dataset with YOLO annotations covering military and civilian objects.
Applied preprocessing to ensure YOLO compatibility (resizing, normalization, augmentation).

#### Model Training
Trained a YOLO model to detect and classify objects such as soldiers, weapons, vehicles, and trenches.

#### Real-Time Detection
Enabled detection from real-time video feeds or uploaded images using the trained model.

#### Threat Classification
Categorized detected objects into threats (e.g., weapons, enemy soldiers) and non-threats (e.g., civilians, friendly soldiers).

#### Streamlit Web Interface
Developed an interactive web app for image/video upload and visualizing detection results.

#### Model Evaluation
Assessed model performance using key metrics like precision, recall, and mAP.
