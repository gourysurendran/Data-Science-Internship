# Data-Science-Internship

CODTECH Data Science Internship Tasks

---

Task 1: Data Pipeline

Objective
To build a data pipeline for preprocessing, transformation, and loading using Pandas and Scikit-learn.

Steps Performed

* Loaded dataset using Pandas
* Handled missing values (Age, Embarked)
* Dropped unnecessary column (Cabin)
* Applied Label Encoding using Scikit-learn
* Saved processed dataset

Tools Used

* Python
* Pandas
* Scikit-learn

Output

* processed_data.csv (cleaned dataset)



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



Task 3: End-to-End Data Science Project - Health Risk Prediction

Objective

To develop a complete data science project, starting from data preprocessing and model building to deploying a machine learning model as a web application using Flask.



Dataset

The dataset contains health-related attributes used to predict risk levels, including:

Age

Body Mass Index (BMI)

Blood Pressure (BP)



---

Steps Performed

1. Loaded and explored the dataset


2. Cleaned data and handled missing values


3. Selected relevant features (Age, BMI, BP)


4. Trained a machine learning model (e.g., Random Forest / Logistic Regression — update if needed)


5. Evaluated model performance


6. Saved the trained model using pickle (model.pkl)


7. Developed a Flask web application


8. Created a user interface using HTML


9. Integrated the model with the backend


10. Deployed the application using Render




---

Tools Used

Python

Pandas

Scikit-learn

Flask

HTML

Gunicorn

Render



---

Output

Live Web Application
👉 https://riskwiseai.onrender.com

Model File
👉 model.pkl

Web Interface
👉 templates/index.html



---

Model Details

Input Features: Age, BMI, BP

Output: Health Risk Level (Low / Medium / High)

Model Type: Machine Learning Classifier



---

Conclusion

The project successfully demonstrates an end-to-end data science workflow by integrating data preprocessing, model development, and deployment into a functional web application. It highlights the ability to convert a machine learning model into a real-world usable system, making predictions accessible through a user-friendly interface.


