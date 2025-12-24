# Knee-osteoarthritis-detection-and-classificatin-using-X-ray-images.
Developed an AI-powered system to detect Knee Osteoarthritis from X-ray images using CNN and Transfer Learning, deployed via Streamlit.
🦵 Knee Osteoarthritis Detection and Classification Using X-Ray Images
📌 Project Overview

Knee Osteoarthritis (OA) is a common degenerative joint disease that affects millions of people worldwide, especially the elderly. Early and accurate diagnosis is essential for effective treatment and improved quality of life.

This project presents an AI-based system for automatic detection and classification of Knee Osteoarthritis using X-ray images. The system leverages Deep Learning and Transfer Learning (InceptionV3) to classify knee X-ray images into Normal and Osteoarthritis categories.
The trained model is deployed as a user-friendly web application using Streamlit, allowing users to upload an X-ray image and receive instant prediction results.
🎯 Objectives

To automate knee osteoarthritis detection using medical imaging

To reduce dependency on manual diagnosis

To assist medical professionals with AI-based decision support

To build an end-to-end ML pipeline from training to deployment

🧠 Technologies Used

Programming Language: Python

Deep Learning Framework: TensorFlow & Keras

Model Architecture: Transfer Learning with InceptionV3

Frontend / Deployment: Streamlit

Image Processing: PIL, NumPy
📂 Project Architecture
Knee-Osteoarthritis-Detection/
│
├── dataset/
│   ├── train/
│   └── test/
│
├── model_training.py
├── app.py
├── model.h5
├── background/
│   └── 1.png
│
├── requirements.txt
└── README.md
🧪 Dataset Description

The dataset consists of Knee X-ray images

Two classes:

Normal

Osteoarthritis

Dataset is organized into training, validation, and testing folders

Images are resized to 75×75 and normalized

🔄 Image Preprocessing & Augmentation

Image resizing and normalization

Data augmentation techniques:

Rotation

Zooming

Width & height shifting

Augmentation helps improve model generalization and reduces overfitting
📊 Results

The model achieves good accuracy in classifying knee X-ray images

Data augmentation and dropout helped reduce overfitting

The trained model generalizes well on unseen test data

🌐 Web Application

A Streamlit-based web application is developed for deployment:

Users can upload knee X-ray images

The image is preprocessed and passed to the trained model

Prediction result is displayed as:

Normal

Osteoarthritis

The application includes a visually enhanced interface with background styling
🔍 Explainability (Grad-CAM)

Grad-CAM was studied as an explainable AI technique

It helps visualize regions of the X-ray image that influence model predictions

Heatmaps highlight clinically relevant areas such as knee joints

Future work includes full integration of Grad-CAM into the application
Visualization: Grad-CAM (concept studied for explainability)

