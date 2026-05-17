# Data-Science-Internship

CODTECH Data Science Internship Tasks

---

# Task 1: Data Pipeline

## Objective
To build a data preprocessing and transformation pipeline using Pandas and Scikit-learn.

## Steps Performed
- Loaded dataset using Pandas
- Handled missing values
- Removed unnecessary columns
- Applied Label Encoding
- Saved cleaned dataset

## Tools Used
- Python
- Pandas
- Scikit-learn

## Output
- Processed and cleaned dataset (`processed_data.csv`)

---

# Task 2: Deep Learning - MNIST Digit Classification

## Objective
To develop a deep learning model for handwritten digit classification using the MNIST dataset.

## Dataset
The MNIST dataset contains grayscale images of handwritten digits (0–9).

## Steps Performed
- Imported TensorFlow and Keras libraries
- Loaded and visualized the dataset
- Normalized image pixel values
- Built and trained a neural network model
- Evaluated model accuracy
- Visualized predictions

## Model Architecture
- Input Layer: Flatten (28×28)
- Hidden Layer: Dense (128, ReLU)
- Output Layer: Dense (10, Softmax)

## Results
- Achieved approximately 97% accuracy on the test dataset

## Tools Used
- Python
- TensorFlow
- Keras
- Matplotlib

---

# Task 3: End-to-End Data Science Project - Health Risk Prediction Web Application

## Objective
To develop a complete end-to-end machine learning web application using Flask.

## Project Overview
This project predicts a user's overall health risk level (Low, Medium, High) using:
- Age
- BMI
- Blood Pressure

The application integrates machine learning, Flask backend development, and deployment into a real-world usable system.

## Features
- User-friendly web interface
- Real-time prediction system
- Input validation
- Health risk explanation
- API endpoint support
- Render deployment

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Flask
- HTML/CSS
- Gunicorn
- Render

## Live Demo
🔗 https://riskwiseai.onrender.com

## GitHub Repository
🔗 https://github.com/gourysurendran/Task3_Health_App

---

# Task 4: Hospital Resource Optimization Using Linear Programming

## Objective
To solve a hospital resource allocation problem using optimization techniques and Linear Programming with the PuLP library in Python.

## Problem Statement
Hospitals often face challenges in efficiently allocating limited resources such as doctors, nurses, and hospital beds across different departments. Improper allocation can lead to increased operational costs and reduced healthcare efficiency.

This project optimizes the allocation of doctors across hospital departments such as ICU, Emergency, and General Ward while minimizing staffing costs and satisfying staffing constraints.

## Optimization Technique
- Linear Programming

## Tools Used
- Python
- PuLP
- Pandas
- Matplotlib
- Jupyter Notebook

## Features
- Hospital staffing optimization
- Constraint-based resource allocation
- Cost minimization
- Department-wise doctor allocation
- Graphical visualization of optimized allocation

## Project Workflow
1. Problem Setup
2. Define Decision Variables
3. Create Objective Function
4. Add Constraints
5. Solve Optimization Model
6. Display Optimized Results
7. Generate Insights and Visualizations

## Output
- Optimized doctor allocation
- Staffing cost minimization
- Department-wise allocation graph
- Operational insights

## Conclusion
This project demonstrates how Linear Programming and optimization techniques can be applied to solve real-world healthcare resource management problems efficiently.

---

## Author
Goury Surendran