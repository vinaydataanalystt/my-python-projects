

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ---------------------------------------------------------------
# STEP 1: CREATE THE STUDENT DATA (only the first time)
# ---------------------------------------------------------------
# If you have a real dataset, save it as student_placement.csv with
# the same column names and this step will be skipped.

FILE = "student_placement.csv"

if not os.path.exists(FILE):
    np.random.seed(1)
    n = 500

    cgpa = np.round(np.random.uniform(5.0, 10.0, n), 1)
    iq = np.random.randint(80, 141, n)
    internships = np.random.randint(0, 4, n)
    projects = np.random.randint(0, 6, n)
    communication = np.random.randint(1, 11, n)
    backlogs = np.random.randint(0, 4, n)

    # A score decides the chance of getting placed
    score = (
        1.2 * (cgpa - 7.5)
        + 0.03 * (iq - 110)
        + 0.6 * internships
        + 0.3 * projects
        + 0.25 * (communication - 5)
        - 0.8 * backlogs
    )
    chance = 1 / (1 + np.exp(-score))
    placed = (np.random.rand(n) < chance).astype(int)

    data = pd.DataFrame({
        "cgpa": cgpa,
        "iq": iq,
        "internships": internships,
        "projects": projects,
        "communication": communication,
        "backlogs": backlogs,
        "placed": placed,
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
print("\nPlaced (1) and Not placed (0):")
print(df["placed"].value_counts())


# ---------------------------------------------------------------
# STEP 3: CHECK AND CLEAN THE DATA
# ---------------------------------------------------------------
print("\n===== STEP 3: CHECK THE DATA =====")
print("Missing values:")
print(df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
print("\nRows after cleaning:", len(df))


# ---------------------------------------------------------------
# STEP 4: SPLIT INTO INPUTS (X) AND ANSWER (y)
# ---------------------------------------------------------------
features = ["cgpa", "iq", "internships", "projects", "communication", "backlogs"]
X = df[features]
y = df["placed"]

# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print("\nTraining rows:", len(X_train), "| Testing rows:", len(X_test))


# ---------------------------------------------------------------
# STEP 5: TRAIN 3 MODELS AND COMPARE
# ---------------------------------------------------------------
print("\n===== STEP 5: TRAIN THE MODELS =====")
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression()),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=1),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=1),
}

best_name = ""
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(name, "accuracy:", round(acc * 100, 1), "%")
    if acc > best_accuracy:
        best_accuracy = acc
        best_name = name

best_model = models[best_name]
print("\nBest model:", best_name, "with", round(best_accuracy * 100, 1), "% accuracy")


# ---------------------------------------------------------------
# STEP 6: CHECK THE BEST MODEL IN DETAIL
# ---------------------------------------------------------------
print("\n===== STEP 6: DETAILED RESULTS =====")
best_predictions = best_model.predict(X_test)

print("Confusion matrix:")
print(confusion_matrix(y_test, best_predictions))
print("\nClassification report:")
print(classification_report(y_test, best_predictions))


# ---------------------------------------------------------------
# STEP 7: CHARTS
# ---------------------------------------------------------------
# Which features matter most? (from the Random Forest)
forest = models["Random Forest"]
importance = pd.Series(forest.feature_importances_, index=features).sort_values()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

importance.plot(kind="barh", ax=axes[0], color="teal")
axes[0].set_title("Which features matter most?")
axes[0].set_xlabel("Importance")

axes[1].hist([df[df["placed"] == 1]["cgpa"], df[df["placed"] == 0]["cgpa"]],
             bins=8, label=["Placed", "Not placed"], color=["green", "red"])
axes[1].set_title("CGPA of placed vs not placed students")
axes[1].set_xlabel("CGPA")
axes[1].set_ylabel("Number of students")
axes[1].legend()

plt.tight_layout()
plt.savefig("placement_charts.png")
print("\nChart saved as placement_charts.png")

print("\nMost important feature:", importance.index[-1])


# ---------------------------------------------------------------
# STEP 8: PREDICT FOR A NEW STUDENT
# ---------------------------------------------------------------
print("\n===== STEP 8: PREDICT FOR A NEW STUDENT =====")
cgpa = float(input("Enter CGPA (5 to 10): "))
iq = float(input("Enter IQ (80 to 140): "))
internships = float(input("Enter number of internships (0 to 3): "))
projects = float(input("Enter number of projects (0 to 5): "))
communication = float(input("Enter communication skill (1 to 10): "))
backlogs = float(input("Enter number of backlogs (0 to 3): "))

student = pd.DataFrame([[cgpa, iq, internships, projects, communication, backlogs]], columns=features)
answer = best_model.predict(student)[0]
chance = best_model.predict_proba(student)[0][1]

print("\nChance of placement:", round(chance * 100, 1), "%")
if answer == 1:
    print("Result: The student is likely to be PLACED.")
else:
    print("Result: The student is likely NOT to be placed.")

plt.show()
