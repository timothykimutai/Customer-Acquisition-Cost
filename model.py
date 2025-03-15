from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from data_loader import df

# Convert CAC to numeric
df["CAC"]= df["CAC"].astype(float)

# Feature & Target
features = ["ad_spend", "clicks", "conversions", "impressions"]
X = df[features]
y= df["CAC"]

# Check if there are missing values
print("Missing values in y:", y.isnull().sum())

# Train-Test Split
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, y_pred)
print(f"Model MAAE: {mae:.2f}")

# Save the Model
import joblib
joblib.dump(model, "models/cac model.pkl")