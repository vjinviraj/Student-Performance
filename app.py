from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = pickle.load(open("student_performance_model.pkl", "rb"))

@app.route("/")
def home():
    return "Student Performance Predictor API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Get JSON data from frontend
        study_hours = float(data["study_hours"])
        previous_score = float(data["previous_score"])

        # Make prediction
        features = np.array([[study_hours, previous_score]])
        prediction = model.predict(features)[0]

        # Convert prediction to readable format
        result = "Pass" if prediction == 1 else "Fail"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
