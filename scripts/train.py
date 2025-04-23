import logging
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import os

# Configure logging before doing anything else
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Get the project root directory (one level up from scripts)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load the California Housing dataset
logging.info("Loading California Housing dataset")
housing = fetch_california_housing()
X = housing.data
y = housing.target

# Feature names for reference
feature_names = housing.feature_names
logging.info(f"Feature names: {feature_names}")

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple linear regression model
logging.info("Training linear regression model")
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate performance
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Save the model using absolute path
model_path = os.path.join(PROJECT_ROOT, 'models', 'ml_model.pkl')
pickle.dump(model, open(model_path, 'wb'))

# Log important messages
logging.info(f"Model Mean Squared Error: {mse:.4f}")
logging.info(f"Model Root Mean Squared Error: {rmse:.4f}")
logging.info(f"Model R² Score: {r2:.4f}")
logging.info("Model saved as ml_model.pkl")
