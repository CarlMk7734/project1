import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
data = {
    'Video_Duration': [10, 15, 20, 12, 18],
    'Hashtags': ['travel', 'fitness', 'food', 'art', 'fashion'],
    'Description_Length': [120, 80, 150, 90, 110],
    'Views': [5000, 7500, 10000, 6000, 8000],
    'Likes': [200, 300, 400, 250, 350],
    'Comments': [30, 40, 50, 35, 45],
    'Shares': [10, 15, 20, 12, 18],
    'Engagement_Rate': [0.046, 0.053, 0.055, 0.048, 0.051]
}

df = pd.DataFrame(data)

# Select relevant features and target variable
features = ['Video_Duration', 'Description_Length', 'Likes', 'Comments', 'Shares', 'Engagement_Rate']
target = 'Views'

X = df[features]
y = df[target]

# Create and train a Random Forest Regressor model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# Make predictions on the same data for simplicity (not recommended for real-world evaluation)
y_pred = model.predict(X)

# Evaluate the model
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
