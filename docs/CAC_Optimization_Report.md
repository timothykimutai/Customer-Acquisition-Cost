# Comprehensive Report: Data-Driven Customer Acquisition Cost (CAC) Optimization for E-commerce

## 1. Introduction
E-commerce businesses invest heavily in marketing campaigns to acquire new customers. However, optimizing Customer Acquisition Cost (CAC) while maintaining profitability remains a challenge. This project presents a data-driven solution that leverages machine learning and optimization techniques to reduce CAC and improve Return on Investment (ROI).

### Objectives:
- Analyze marketing and sales data to derive insights.
- Build a predictive model for CAC estimation.
- Optimize ad spend allocation across platforms.
- Deploy an API and interactive dashboard for real-time recommendations.

![E-commerce Growth](https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)

## 2. Data Sources & Preprocessing
We use two key datasets:

1. **Marketing Data (`marketing_data.csv`)**:
   - `platform`: Advertising platform (Google, Facebook, etc.).
   - `ad_spend`: Amount spent on ads.
   - `clicks`: Number of ad clicks.
   - `conversions`: Number of successful customer acquisitions.
   - `impressions`: Total number of ad views.

2. **Sales Data (`sales_data.csv`)**:
   - `customer_id`: Unique customer identifier.
   - `total_revenue`: Revenue generated from the customer.
   - `repeat_purchases`: Number of times the customer made repeat purchases.

### Data Cleaning & Feature Engineering:
- Merging `marketing_data` and `sales_data` on `customer_id`.
- Creating key metrics:
  - **Customer Acquisition Cost (CAC)** = `ad_spend / conversions`
  - **Customer Lifetime Value (LTV)** = `total_revenue / unique_customers`
  - **Return on Investment (ROI)** = `(total_revenue - ad_spend) / ad_spend`
- Handling missing values by imputing with mean values.

![Data Pipeline](https://cdn.pixabay.com/photo/2023/01/16/20/50/geometry-7723324_1280.jpg)

## 3. Exploratory Data Analysis (EDA)
EDA helps us understand trends and relationships between marketing spend and customer behavior.

- **CAC Distribution:** Histogram visualization.
- **CAC vs LTV:** Scatter plot with platform-based color coding.
- **Platform Performance:** Bar chart comparing CAC across advertising platforms.

![CAC Distribution](./images/cac_distribution.png)

## 4. Predictive Modeling: CAC Estimation
A machine learning model is trained to predict CAC based on ad-related features.

### Model Selection:
We use **RandomForestRegressor** due to its high accuracy and ability to handle non-linear relationships.

### Training Process:
1. Define Features (`X`) and Target (`y`):
   - Features: `ad_spend`, `clicks`, `conversions`, `impressions`
   - Target: `CAC`
2. Split Data (80% Train / 20% Test)
3. Train the Random Forest model.
4. Evaluate Model Performance (Mean Absolute Error, MAE).
5. Save the model using `joblib` for deployment.

![Machine Learning Model](https://cdn.pixabay.com/photo/2024/01/29/22/47/ai-generated-8540915_1280.jpg)

## 5. Budget Optimization Strategy
An optimization function is created to allocate the marketing budget effectively:

- Assign more budget to platforms with **lower CAC**.
- Use an **inverse proportional allocation** strategy.

![Budget Optimization](https://cdn.pixabay.com/photo/2021/01/07/11/17/investment-5896895_1280.jpg)

## 6. Deployment: API & Dashboard
### 6.1 API Development (Flask)
A REST API is built to serve model predictions and optimization insights.

#### Endpoints:
- **`/predict`**: Accepts input features and returns predicted CAC.
- **`/optimize`**: Accepts budget and suggests the best allocation.

### 6.2 Interactive Dashboard (Dash)
A web dashboard provides real-time visualizations for CAC trends and budget allocation.

#### Features:
- **Filterable CAC Analysis by Platform**
- **Graphical Budget Optimization Insights**
- **Dark Mode UI for better readability**

![Dashboard Interface](./images/dashboard.png)

## 7. Conclusion
This project provides an end-to-end solution for **CAC optimization in e-commerce** using machine learning, optimization strategies, and real-time analytics. The approach helps businesses **reduce costs, maximize ROI, and improve marketing efficiency**.

### Key Takeaways:
✅ **Data-Driven Insights**: Understand marketing effectiveness.
✅ **AI-Powered Predictions**: Estimate CAC before running campaigns.
✅ **Smart Budget Allocation**: Optimize ad spend dynamically.
✅ **Real-Time Decision Making**: Deploy as an API and Dashboard.

By leveraging this framework, businesses can make **smarter marketing investments** and enhance profitability.

