

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# ---------------------------------------------------------------
# STEP 1: CREATE THE ELECTRICITY DATA (only the first time)
# ---------------------------------------------------------------
# If you have a real dataset, save it as electricity_data.csv with
# the same column names and this step will be skipped.

FILE = "electricity_data.csv"

if not os.path.exists(FILE):
    np.random.seed(7)
    n = 600

    temperature = np.round(np.random.uniform(15, 42, n), 1)
    humidity = np.random.randint(20, 91, n)
    members = np.random.randint(1, 9, n)
    appliances = np.random.randint(3, 21, n)
    weekend = np.random.randint(0, 2, n)

    # Units used: more heat (AC), more people and more appliances = more units
    units = (
        4
        + 0.35 * temperature
        + 1.2 * np.maximum(temperature - 28, 0)
        + 2.2 * members
        + 0.9 * appliances
        + 2.0 * weekend
        + 0.03 * humidity
        + np.random.normal(0, 2, n)
    )

    data = pd.DataFrame({
        "temperature": temperature,
        "humidity": humidity,
        "members": members,
        "appliances": appliances,
        "weekend": weekend,
        "units": np.round(units, 1),
    })
    data.to_csv(FILE, index=False)
    print("Sample data created:", FILE)


# ---------------------------------------------------------------
# STEP 2: LOAD AND LOOK AT THE DATA
# ---------------------------------------------------------------
print("\n===== STEP 2: LOAD THE DATA =====")
df = pd.read_csv(FILE)
print(df.head())
print("\nRows and columns:", df.shape)
print("\nSummary of the numbers:")
print(df.describe().round(2))


# ---------------------------------------------------------------
# STEP 3: CHECK AND CLEAN THE DATA
# ---------------------------------------------------------------
print("\n===== STEP 3: CHECK THE DATA =====")
print("Missing values:")
print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
print("\nRows after cleaning:", len(df))

print("\nHow each column is related to units:")
print(df.corr()["units"].round(2))


# ---------------------------------------------------------------
# STEP 4: SPLIT INTO INPUTS (X) AND ANSWER (y)
# ---------------------------------------------------------------
features = ["temperature", "humidity", "members", "appliances", "weekend"]
X = df[features]
y = df["units"]

# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print("\nTraining rows:", len(X_train), "| Testing rows:", len(X_test))


# ---------------------------------------------------------------
# STEP 5: TRAIN 3 MODELS AND COMPARE
# ---------------------------------------------------------------
print("\n===== STEP 5: TRAIN THE MODELS =====")
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=6, random_state=1),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=1),
}

best_name = ""
best_r2 = -999

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    print(name)
    print("   R2 score:", round(r2, 3), "| MAE:", round(mae, 2), "units | RMSE:", round(rmse, 2), "units")
    if r2 > best_r2:
        best_r2 = r2
        best_name = name

best_model = models[best_name]
print("\nBest model:", best_name, "with R2 score", round(best_r2, 3))


# ---------------------------------------------------------------
# STEP 6: SEE HOW THE BEST MODEL PREDICTS
# ---------------------------------------------------------------
print("\n===== STEP 6: ACTUAL vs PREDICTED (first 8 test days) =====")
best_predictions = best_model.predict(X_test)
compare = pd.DataFrame({
    "Actual": y_test.values[:8],
    "Predicted": best_predictions[:8].round(1),
})
compare["Difference"] = (compare["Actual"] - compare["Predicted"]).round(1)
print(compare)


# ---------------------------------------------------------------
# STEP 7: CHARTS
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Chart 1: actual vs predicted
axes[0].scatter(y_test, best_predictions, color="blue", alpha=0.6)
low = min(y_test.min(), best_predictions.min())
high = max(y_test.max(), best_predictions.max())
axes[0].plot([low, high], [low, high], color="red")
axes[0].set_title("Actual vs Predicted (" + best_name + ")")
axes[0].set_xlabel("Actual units")
axes[0].set_ylabel("Predicted units")

# Chart 2: temperature vs units
axes[1].scatter(df["temperature"], df["units"], color="orange", alpha=0.5)
axes[1].set_title("Temperature vs Units used")
axes[1].set_xlabel("Temperature (C)")
axes[1].set_ylabel("Units (kWh)")

# Chart 3: which features matter most
forest = models["Random Forest"]
importance = pd.Series(forest.feature_importances_, index=features).sort_values()
importance.plot(kind="barh", ax=axes[2], color="teal")
axes[2].set_title("Which features matter most?")
axes[2].set_xlabel("Importance")

plt.tight_layout()
plt.savefig("electricity_charts.png")
print("\nChart saved as electricity_charts.png")
print("Most important feature:", importance.index[-1])


# ---------------------------------------------------------------
# STEP 8: PREDICT FOR A NEW DAY
# ---------------------------------------------------------------
print("\n===== STEP 8: PREDICT ELECTRICITY USE =====")
temperature = float(input("Enter temperature in C (15 to 42): "))
humidity = float(input("Enter humidity % (20 to 90): "))
members = float(input("Enter number of family members (1 to 8): "))
appliances = float(input("Enter number of appliances (3 to 20): "))
weekend = float(input("Is it a weekend? (1 = yes, 0 = no): "))

day = pd.DataFrame([[temperature, humidity, members, appliances, weekend]], columns=features)
result = best_model.predict(day)[0]

print("\nPredicted electricity use:", round(result, 1), "units (kWh)")
print("Estimated bill for the day at Rs 7 per unit: Rs", round(result * 7))

plt.show()