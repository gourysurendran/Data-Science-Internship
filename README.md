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