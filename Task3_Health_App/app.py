from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
try:
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        age = int(request.form["age"])
        bmi = float(request.form["bmi"])
        bp = int(request.form["bp"])

        # Input validation
        if age <= 0 or age > 120:
            return render_template(
                "index.html",
                prediction_text="Invalid Age",
                explanation_text="Please enter a valid age.",
                age=age, bmi=bmi, bp=bp
            )

        if bmi <= 0 or bmi > 60:
            return render_template(
                "index.html",
                prediction_text="Invalid BMI",
                explanation_text="Please enter a realistic BMI value.",
                age=age, bmi=bmi, bp=bp
            )

        if bp <= 0 or bp > 250:
            return render_template(
                "index.html",
                prediction_text="Invalid Blood Pressure",
                explanation_text="Please enter a realistic BP value.",
                age=age, bmi=bmi, bp=bp
            )

        # Create dataframe
        features = pd.DataFrame([[age, bmi, bp]],
                                columns=["Age", "BMI", "BP"])

        # Predict
        prediction = model.predict(features)[0]

        # Result mapping
        result_map = {
            0: "Low Health Risk",
            1: "Medium Health Risk",
            2: "High Health Risk"
        }

        result = result_map.get(prediction, "Unknown")

        # Explanation mapping
        explanation_map = {
            0: "Your health indicators appear to be within a generally healthy range.",
            1: "Some health indicators may require attention. Maintaining a healthy lifestyle is recommended.",
            2: "Your health indicators suggest elevated health risk levels. Consider consulting a healthcare professional."
        }

        explanation = explanation_map.get(prediction, "")

        return render_template(
            "index.html",
            prediction_text=result,
            explanation_text=explanation,
            age=age, bmi=bmi, bp=bp
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text="Error occurred",
            explanation_text=str(e),
            age=request.form.get("age", ""),
            bmi=request.form.get("bmi", ""),
            bp=request.form.get("bp", "")
        )


# API Endpoint
@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        age = int(data["age"])
        bmi = float(data["bmi"])
        bp = int(data["bp"])

        features = pd.DataFrame([[age, bmi, bp]],
                                columns=["Age", "BMI", "BP"])

        prediction = model.predict(features)[0]

        result_map = {
            0: "Low Health Risk",
            1: "Medium Health Risk",
            2: "High Health Risk"
        }

        result = result_map.get(prediction, "Unknown")

        return {
            "prediction": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


if __name__ == "__main__":
    app.run(debug=False)