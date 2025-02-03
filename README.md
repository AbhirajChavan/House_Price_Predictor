# 🏡 House Price Prediction - Flask Web App

This project demonstrates a **step-by-step implementation** of a **Flask web application** for **house price prediction** using a **machine learning model**. The model is trained on the `india_housing_prices.csv` dataset and deployed using Flask.

## 📌 Features

- Load and explore the dataset in **Jupyter Lab**.
- Preprocess the data by handling missing values, encoding categorical variables, and normalizing numerical features.
- Train a **Linear Regression** model.
- Save the trained model using **joblib** for later use in the Flask application.
- Develop a **Flask web app** to serve the trained model.
- Build an **HTML form** for user input.
- Deploy the app locally for real-time house price predictions.

---

## 📂 Project Structure

```bash
house_price_prediction/
│── templates/              # HTML templates
│   ├── index.html          # User input form & prediction display
│── app.py                  # Flask application
│── house_price_model.pkl   # Saved machine learning model
│── scaler.pkl              # Saved scaler for feature normalization
│── label_encoders.pkl      # Saved label encoders for categorical variables
│── india_housing_prices.csv # Dataset
│── requirements.txt        # Dependencies list                        
│── README.md               # Project documentation


