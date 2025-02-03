from flask import Flask, render_template, request
import joblib
import numpy as np

# Loading 
model = joblib.load("house_price_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Number of expected features
num_features = scaler.n_features_in_

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        features = []

        # Extracting input values from form
        bhk = request.form["BHK"]
        size = request.form["Size_in_SqFt"]
        city = request.form["City"]

        # Convert numerical values to float
        features.append(float(bhk))
        features.append(float(size))

        # Encode City (Categorical Variable)
        if "City" in label_encoders:
            if city in label_encoders["City"].classes_:
                city_encoded = label_encoders["City"].transform([city])[0]
            else:
                city_encoded = 0  # Default encoding for new/unseen cities
            features.append(city_encoded)

        # To ensure correct feature count before scaling
        if len(features) != num_features:
            return "Error: Incorrect number of input features!", 400

        # Scale the input features
        features_scaled = scaler.transform([features])

        # Predict house price
        prediction = model.predict(features_scaled)[0]

        return render_template("index.html", prediction=round(prediction, 2))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
