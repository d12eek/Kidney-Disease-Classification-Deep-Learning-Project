# Kidney Disease Classification Deep Learning Project

End-to-end deep learning project to classify kidney CT scan images as Normal or Tumor.
# Kidney Disease Classification - Deep Learning Project

## Overview
An end-to-end deep learning project for classifying kidney CT scan images as **Normal** or **Tumor** using VGG16 transfer learning.

## Tech Stack
- **Model**: VGG16 (Transfer Learning)
- **Framework**: TensorFlow/Keras
- **Experiment Tracking**: MLflow
- **Web App**: Flask
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (ECR + EC2)

## Pipeline
1. Data Ingestion
2. Base Model Preparation (VGG16)
3. Model Training
4. Model Evaluation + MLflow Logging
5. Flask Web App
6. Docker + AWS Deployment

## Results
- **Accuracy**: ~72.5%
- **Dataset**: 7,360 CT scan images (Normal + Tumor)

## How to Run Locally
```bash
git clone https://github.com/d12eek/Kidney-Disease-Classification-Deep-Learning-Project.git
cd Kidney-Disease-Classification-Deep-Learning-Project
pip install -r requirements.txt
python app.py
```

## Web App
Upload a kidney CT scan image → Get instant Normal/Tumor prediction