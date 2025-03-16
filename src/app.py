from flask import Flask, request, jsonify
import joblib
import numpy as np
from optimizer import optimize_budget
from data_loader import df
# app
app = Flask(__name__)

# load model
model = joblib.load("models/cac model.pkl")

@app.route("/predict", methods= ["POST"])
def predict_cac():
    data = request.json()
    X_new= np.array([data["ad_spend"], data["clicks"], data["conversions"], data["impressions"]]).reshape(1, -1)
    prediction = model.predict(X_new)
    return jsonify({"predicted_CAC": prediction[0]})

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    budget= data["budget"]
    allocations = optimize_budget(df, budget)
    return jsonify(allocations)
if __name__=="__main__":
    app.run(debug=True)