# E-commerce CAC Optimization
![Python](https://img.shields.io/badge/Python-3.7%20|%203.8%20|%203.9%20|%203.10-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.x-blue?logo=pandas)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

## **Project Overview**
This project aims to help e-commerce businesses optimize their **Customer Acquisition Cost (CAC)** while maximizing **Return on Investment (ROI)**. By leveraging **data analytics, machine learning, and optimization techniques**, this solution provides actionable insights to reduce marketing costs and improve efficiency.

## **Key Features**
✅ Predictive model for CAC estimation  
✅ Budget optimization strategy for ad spend  
✅ REST API for real-time predictions  
✅ Interactive dashboard for visual analysis  
✅ Data-driven insights on marketing performance  

## **Project Structure**
```
/ecommerce_cac_optimization
│── /data                  # Raw marketing and sales data
│── /src                   # Source code
│   ├── data_loader.py     # Data processing and feature engineering
│   ├── model.py           # Machine learning model training
│   ├── optimizer.py       # Budget optimization logic
│   ├── api.py             # Flask API for predictions
│   ├── dashboard.py       # Dash-based interactive dashboard
│── /models                # Trained models
│── /docs                  # Project documentation
│── requirements.txt       # Python dependencies
│── README.md              # Project overview
```

## **Installation**
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/timothykimutai/Customer-Acquisition-Cost.git
cd Customer-Acquisition-Cost
```
### 2️⃣ Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## **Usage**
### **1. Train the Model**
Run the script to process data and train the CAC prediction model:
```bash
python src/model.py
```
### **2. Start the API**
```bash
python src/api.py
```
The API will be available at `http://127.0.0.1:5000/`

### **3. Run the Dashboard**
```bash
python src/dashboard.py
```
Open `http://127.0.0.1:8050/` in your browser.

## **API Endpoints**
| Endpoint      | Method | Description |
|--------------|--------|-------------|
| `/predict`   | POST   | Predicts CAC based on input features |
| `/optimize`  | POST   | Returns budget allocation suggestions |

## **Technologies Used**
- **Python** (Pandas, NumPy, Scikit-learn)
- **Machine Learning** (RandomForestRegressor)
- **Flask** (REST API)
- **Dash & Plotly** (Interactive Dashboard)
- **Optimization Algorithms**

## **License**
This project is licensed under the MIT License.

## **Author & Contact**
**Author:** Timothy Kimutai 
**Email:** timothykimtai@gmail.com


