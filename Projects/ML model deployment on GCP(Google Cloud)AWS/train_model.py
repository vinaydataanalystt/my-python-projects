# Trains a simple ML model and saves it as model.pkl
# Run:  python train_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load data (iris flower dataset)
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

# 2. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Check accuracy
print("Accuracy:", round(model.score(X_test, y_test), 2))

# 4. Save the model and the flower names
joblib.dump({"model": model, "names": list(data.target_names)}, "model.pkl")
print("Model saved as model.pkl")
