
from sklearn.linear_model import LogisticRegression


# ---------------------------------------------------------------
# PART 1: BASIC LOGISTIC REGRESSION (Programs 1 to 5)
# ---------------------------------------------------------------

def program1():
    # Predict Pass (1) or Fail (0) from study hours
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    answer = model.predict([[5.5]])[0]
    print("Result for 5.5 hours:", "Pass" if answer == 1 else "Fail")


def program2():
    # Show the probability of passing
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    prob = model.predict_proba([[5]])[0][1]
    print("Chance of passing with 5 hours:", round(prob * 100, 1), "%")


def program3():
    # Pass or Fail from user input
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    h = float(input("Enter study hours: "))
    answer = model.predict([[h]])[0]
    print("Prediction:", "Pass" if answer == 1 else "Fail")


def program4():
    # Check the accuracy of the model
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    print("Accuracy:", model.score(hours, result))


def program5():
    # Plot the S-shaped (sigmoid) curve
    import matplotlib.pyplot as plt
    import numpy as np
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 1, 0, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    x = np.linspace(0, 9, 100).reshape(-1, 1)
    plt.scatter(hours, result, color="blue")
    plt.plot(x, model.predict_proba(x)[:, 1], color="red")
    plt.xlabel("Hours studied")
    plt.ylabel("Chance of passing")
    plt.title("Logistic Regression Curve")
    plt.show()


# ---------------------------------------------------------------
# PART 2: MORE THAN ONE INPUT (Programs 6 to 10)
# ---------------------------------------------------------------

def program6():
    # Loan approval from salary and age
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]   # salary in thousands
    model = LogisticRegression()
    model.fit(data, loan)
    answer = model.predict([[65, 38]])[0]
    print("Loan for salary 65k, age 38:", "Approved" if answer == 1 else "Rejected")


def program7():
    # Show coefficients of the model
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(data, loan)
    print("Coefficients:", model.coef_[0].round(3))
    print("Intercept:", model.intercept_.round(3))


def program8():
    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    result = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    x_train, x_test, y_train, y_test = train_test_split(hours, result, test_size=0.3, random_state=1)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    print("Test accuracy:", round(model.score(x_test, y_test), 2))


def program9():
    # Confusion matrix
    from sklearn.metrics import confusion_matrix
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    hours = [[1], [2], [3], [5], [4], [6], [7], [8]]
    model = LogisticRegression()
    model.fit([[1], [2], [3], [4], [5], [6], [7], [8]], [0, 0, 0, 0, 1, 1, 1, 1])
    predicted = model.predict(hours)
    print("Confusion matrix:")
    print(confusion_matrix(actual, predicted))


def program10():
    # Classification report
    from sklearn.metrics import classification_report
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    hours = [[1], [2], [3], [5], [4], [6], [7], [8]]
    model = LogisticRegression()
    model.fit([[1], [2], [3], [4], [5], [6], [7], [8]], [0, 0, 0, 0, 1, 1, 1, 1])
    predicted = model.predict(hours)
    print(classification_report(actual, predicted))


# ---------------------------------------------------------------
# PART 3: METRICS AND DATA (Programs 11 to 15)
# ---------------------------------------------------------------

def program11():
    # Precision, recall and F1 score
    from sklearn.metrics import precision_score, recall_score, f1_score
    actual = [1, 0, 1, 1, 0, 1, 0, 0]
    predicted = [1, 0, 1, 0, 0, 1, 1, 0]
    print("Precision:", round(precision_score(actual, predicted), 2))
    print("Recall:", round(recall_score(actual, predicted), 2))
    print("F1 score:", round(f1_score(actual, predicted), 2))


def program12():
    # Predict for many students at once
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    new = [[2], [4.5], [6], [9]]
    answers = model.predict(new)
    for h, a in zip(new, answers):
        print("Hours:", h[0], "->", "Pass" if a == 1 else "Fail")


def program13():
    # Use a pandas table (DataFrame)
    import pandas as pd
    df = pd.DataFrame({
        "hours": [1, 2, 3, 4, 5, 6, 7, 8],
        "passed": [0, 0, 0, 0, 1, 1, 1, 1],
    })
    print(df)
    model = LogisticRegression()
    model.fit(df[["hours"]], df["passed"])
    print("Prediction for 6 hours:", model.predict(pd.DataFrame({"hours": [6]}))[0])


def program14():
    # Change the decision threshold
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    prob = model.predict_proba([[5]])[0][1]
    print("Probability:", round(prob, 2))
    print("With threshold 0.5:", "Pass" if prob >= 0.5 else "Fail")
    print("With threshold 0.7:", "Pass" if prob >= 0.7 else "Fail")


def program15():
    # Plot two groups of data
    import matplotlib.pyplot as plt
    marks = [30, 35, 40, 45, 55, 60, 70, 80]
    attendance = [50, 55, 60, 65, 70, 80, 85, 90]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    colors = ["red" if r == 0 else "green" for r in result]
    plt.scatter(marks, attendance, c=colors)
    plt.xlabel("Marks")
    plt.ylabel("Attendance %")
    plt.title("Red = Fail, Green = Pass")
    plt.show()


# ---------------------------------------------------------------
# PART 4: REAL-LIFE EXAMPLES (Programs 16 to 20)
# ---------------------------------------------------------------

def program16():
    # Spam detection from number of links and capital words
    data = [[0, 1], [1, 2], [0, 0], [5, 8], [7, 10], [6, 9], [1, 1], [8, 12]]
    spam = [0, 0, 0, 1, 1, 1, 0, 1]
    model = LogisticRegression()
    model.fit(data, spam)
    answer = model.predict([[6, 7]])[0]
    print("Email with 6 links and 7 capital words:", "Spam" if answer == 1 else "Not spam")


def program17():
    # Diabetes prediction from glucose level
    glucose = [[85], [90], [95], [100], [140], [160], [180], [200]]
    diabetes = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(glucose, diabetes)
    g = 150
    answer = model.predict([[g]])[0]
    print("Glucose", g, ":", "Diabetic" if answer == 1 else "Not diabetic")


def program18():
    # Will the customer buy? (age and salary)
    data = [[19, 20], [22, 25], [25, 30], [30, 40], [35, 80], [40, 90], [45, 100], [50, 110]]
    buy = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression(max_iter=1000)
    model.fit(data, buy)
    answer = model.predict([[38, 85]])[0]
    print("Customer age 38, salary 85k:", "Will buy" if answer == 1 else "Will not buy")


def program19():
    # College admission from marks
    marks = [[40], [48], [55], [60], [72], [80], [88], [95]]
    admit = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(marks, admit)
    m = float(input("Enter your marks: "))
    answer = model.predict([[m]])[0]
    print("Admission:", "Selected" if answer == 1 else "Not selected")


def program20():
    # Customer churn (will the customer leave?)
    data = [[1, 5], [2, 4], [3, 3], [10, 1], [12, 0], [11, 1], [2, 5], [14, 0]]
    left = [0, 0, 0, 1, 1, 1, 0, 1]   # [complaints, months active]
    model = LogisticRegression()
    model.fit(data, left)
    answer = model.predict([[9, 1]])[0]
    print("Customer with 9 complaints:", "Will leave" if answer == 1 else "Will stay")


# ---------------------------------------------------------------
# PART 5: IMPROVING THE MODEL (Programs 21 to 25)
# ---------------------------------------------------------------

def program21():
    # Feature scaling
    from sklearn.preprocessing import StandardScaler
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]
    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)
    model = LogisticRegression()
    model.fit(scaled, loan)
    new = scaler.transform([[65, 38]])
    print("Loan prediction:", "Approved" if model.predict(new)[0] == 1 else "Rejected")


def program22():
    # Cross validation
    from sklearn.model_selection import cross_val_score
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    result = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    scores = cross_val_score(LogisticRegression(), hours, result, cv=3)
    print("Scores:", [round(float(s), 2) for s in scores])
    print("Average:", round(float(scores.mean()), 2))


def program23():
    # More than two groups (iris flowers)
    from sklearn.datasets import load_iris
    iris = load_iris()
    model = LogisticRegression(max_iter=1000)
    model.fit(iris.data, iris.target)
    flower = [[5.1, 3.5, 1.4, 0.2]]
    answer = model.predict(flower)[0]
    print("Flower type:", iris.target_names[answer])


def program24():
    # Effect of the C value (regularization)
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    for c in [0.01, 1, 100]:
        model = LogisticRegression(C=c)
        model.fit(hours, result)
        prob = model.predict_proba([[5]])[0][1]
        print("C =", c, "-> chance of pass at 5 hours:", round(prob, 2))


def program25():
    # ROC AUC score
    from sklearn.metrics import roc_auc_score
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 1, 0, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    probs = model.predict_proba(hours)[:, 1]
    print("ROC AUC score:", round(roc_auc_score(result, probs), 2))


# ---------------------------------------------------------------
# PART 6: MORE PROGRAMS (Programs 26 to 30)
# ---------------------------------------------------------------

def program26():
    # Plot the ROC curve
    import matplotlib.pyplot as plt
    from sklearn.metrics import roc_curve
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 1, 0, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    probs = model.predict_proba(hours)[:, 1]
    fpr, tpr, _ = roc_curve(result, probs)
    plt.plot(fpr, tpr, color="red", label="Model")
    plt.plot([0, 1], [0, 1], "--", label="Random guess")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.show()


def program27():
    # Plot the confusion matrix
    import matplotlib.pyplot as plt
    from sklearn.metrics import ConfusionMatrixDisplay
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    predicted = [0, 0, 0, 1, 1, 1, 0, 1]
    ConfusionMatrixDisplay.from_predictions(actual, predicted)
    plt.title("Confusion Matrix")
    plt.show()


def program28():
    # Sigmoid function written by hand
    import math
    def sigmoid(z):
        return 1 / (1 + math.exp(-z))
    for z in [-5, -2, 0, 2, 5]:
        print("z =", z, "-> sigmoid =", round(sigmoid(z), 3))


def program29():
    # Breast cancer dataset (a real dataset from sklearn)
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    data = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)
    model = LogisticRegression(max_iter=5000)
    model.fit(x_train, y_train)
    print("Accuracy on cancer data:", round(model.score(x_test, y_test), 2))


def program30():
    # Save the model to a file and load it again
    import pickle
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = LogisticRegression()
    model.fit(hours, result)
    with open("logistic_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved as logistic_model.pkl")
    with open("logistic_model.pkl", "rb") as f:
        loaded = pickle.load(f)
    print("Loaded model says 7 hours:", "Pass" if loaded.predict([[7]])[0] == 1 else "Fail")


# ---------------------------------------------------------------
# MENU: type a number to run that program
# ---------------------------------------------------------------

programs = {
    1: program1, 2: program2, 3: program3, 4: program4, 5: program5,
    6: program6, 7: program7, 8: program8, 9: program9, 10: program10,
    11: program11, 12: program12, 13: program13, 14: program14, 15: program15,
    16: program16, 17: program17, 18: program18, 19: program19, 20: program20,
    21: program21, 22: program22, 23: program23, 24: program24, 25: program25,
    26: program26, 27: program27, 28: program28, 29: program29, 30: program30,
}

print("30 Programs in Logistic Regression")
choice = int(input("Enter program number (1-30): "))

if choice in programs:
    print("\n--- Program", choice, "---")
    programs[choice]()
else:
    print("Please enter a number between 1 and 30.")