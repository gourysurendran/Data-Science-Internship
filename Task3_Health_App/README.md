# Health Risk Prediction System - End-to-End Data Science Project

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App%20%26%20API-green.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)

**CODTECH IT SOLUTIONS INTERNSHIP - TASK 3**

## 📌 Project Overview
This project is an **End-to-End Data Science Project** demonstrating the full lifecycle of a machine learning model, from data collection and preprocessing to model deployment. The final deliverable is a functional **Web App** and a **RESTful API** built using **Flask**.

The model predicts an individual's **Health Risk Level** (Low, Medium, or High) based on three key metrics:
- Age
- BMI (Body Mass Index)
- Blood Pressure (BP)

## ✨ Features
1. **Machine Learning Pipeline (`health_model.ipynb`)**:
   - Data collection and creation of structured health metrics.
   - Preprocessing and feature selection.
   - Model training using a `RandomForestClassifier`.
   - Serialization of the model using `pickle` (`model.pkl`).
2. **Interactive Web App**:
   - A modern, responsive, glass-morphism designed frontend (`index.html`).
   - Allows users to input their data and receive real-time predictions.
3. **REST API Endpoint (`/api/predict`)**:
   - Accepts JSON data and returns predictions.
   - Ideal for integration with mobile apps, dashboards, or external services.

---

## 🛠️ Project Structure
```
Task3_Health_App/
│
├── health_model.ipynb    # Jupyter Notebook: Data collection, EDA, preprocessing, and model training
├── model.pkl             # Serialized Machine Learning model (Random Forest)
├── app.py                # Flask application (Web App & API routing)
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment configuration for PaaS (e.g., Heroku)
└── templates/
    └── index.html        # Frontend HTML/CSS for the Web App
```

---

## 🚀 How to Run Locally

### 1. Prerequisites
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Retraining the Model (Optional)
If you want to view the data collection and preprocessing steps, open the Jupyter Notebook:
```bash
jupyter notebook health_model.ipynb
```
Run the cells to generate a fresh `model.pkl`.

### 3. Running the Flask App
Start the deployment server:
```bash
python app.py
```
*The app will be accessible at `http://127.0.0.1:5000/`.*

---

## 📡 API Usage
The project includes a fully functional REST API for programmatic access.

**Endpoint:** `/api/predict`
**Method:** `POST`
**Content-Type:** `application/json`

**Example Request:**
```json
{
  "age": 45,
  "bmi": 28.5,
  "bp": 140
}
```

**Example Response:**
```json
{
  "prediction": "Medium Risk",
  "status": "success"
}
```

---

## 🎓 Deliverable Fulfillment
This repository fulfills the CODTECH Task 3 requirements:
- **Data Collection & Preprocessing**: Handled via pandas in `health_model.ipynb`.
- **Model Deployment**: Deployed using the Flask web framework (`app.py`).
- **Showcasing Functionality**: Users can interact directly via the Web GUI (`/`) or the API (`/api/predict`).
