# Data-Science-Internship

CODTECH Data Science Internship Tasks

---

# Task 1: Data Pipeline

## Objective
To build a data pipeline for preprocessing, transformation, and loading using Pandas and Scikit-learn.

## Steps Performed
1. Loaded dataset using Pandas  
2. Handled missing values (Age, Embarked)  
3. Dropped unnecessary column (Cabin)  
4. Applied Label Encoding using Scikit-learn  
5. Saved processed dataset  

## Tools Used
- Python  
- Pandas  
- Scikit-learn  

## Output
- `processed_data.csv` (cleaned dataset)

---

# Task 2: Deep Learning - MNIST Digit Classification

## Objective
To build a deep learning model to classify handwritten digits using the MNIST dataset.

## Dataset
The MNIST dataset contains 28x28 grayscale images of handwritten digits (0–9).

## Steps Performed
1. Imported required libraries (TensorFlow, Keras, Matplotlib)  
2. Loaded the MNIST dataset  
3. Visualized sample images  
4. Normalized pixel values (0–255 → 0–1)  
5. Built a neural network model  
6. Compiled the model  
7. Trained the model  
8. Evaluated model performance  
9. Visualized predictions  

## Model Details
- Input Layer: Flatten (28x28)  
- Hidden Layer: Dense (128, ReLU)  
- Output Layer: Dense (10, Softmax)  

## Results
- Accuracy: ~97%  
- The model correctly classifies most digits  

## Conclusion
The deep learning model successfully performs handwritten digit classification with high accuracy. Visualization confirms correct predictions.

---

# Task 3: End-to-End Data Science Project - Health Risk Prediction Web Application

## Objective
To develop a complete end-to-end data science solution that integrates data preprocessing, machine learning model development, and deployment using Flask.

## Project Overview
This project predicts a user’s health risk level (Low, Medium, High) based on:
- Age  
- Body Mass Index (BMI)  
- Blood Pressure (BP)  

The application demonstrates how a machine learning model can be transformed into a real-world usable web application.

## Steps Performed
1. Loaded and explored the dataset  
2. Cleaned and preprocessed data  
3. Selected relevant features (Age, BMI, BP)  
4. Trained a machine learning classification model  
5. Evaluated model performance  
6. Saved trained model using `pickle` (`model.pkl`)  
7. Developed Flask backend application  
8. Created frontend interface using HTML  
9. Integrated model with Flask  
10. Deployed the application using Render  

## Tools Used
- Python  
- Pandas  
- Scikit-learn  
- Flask  
- HTML/CSS  
- Gunicorn  
- Render  

## Project Structure
```text
Task3_Health_App/
│── app.py
│── model.pkl
│── requirements.txt
│── Procfile
│── health_model.ipynb
│── templates/
│   └── index.html

Live Application

👉 https://riskwiseai.onrender.com

Output

Health Risk Prediction Web Application

Real-time prediction system using Machine Learning


Conclusion

This project demonstrates the complete lifecycle of a data science application, including preprocessing, model training, backend integration, deployment, and user interaction. It highlights practical implementation skills in machine learning, Flask development, and cloud deployment.

