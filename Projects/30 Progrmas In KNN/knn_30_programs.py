

from sklearn.neighbors import KNeighborsClassifier


# ---------------------------------------------------------------
# PART 1: BASIC KNN (Programs 1 to 5)
# ---------------------------------------------------------------

def program1():
    # Predict Pass (1) or Fail (0) from study hours
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    answer = model.predict([[5.5]])[0]
    print("Result for 5.5 hours:", "Pass" if answer == 1 else "Fail")


def program2():
    # Predict using two inputs: hours studied and attendance
    data = [[1, 50], [2, 55], [3, 60], [4, 65], [5, 75], [6, 80], [7, 85], [8, 90]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, result)
    answer = model.predict([[5, 70]])[0]
    print("5 hours, 70% attendance:", "Pass" if answer == 1 else "Fail")


def program3():
    # Pass or Fail from user input
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    h = float(input("Enter study hours: "))
    answer = model.predict([[h]])[0]
    print("Prediction:", "Pass" if answer == 1 else "Fail")


def program4():
    # Check the accuracy of the model
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    print("Accuracy:", model.score(hours, result))


def program5():
    # Find the nearest neighbors of a new point
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    distances, positions = model.kneighbors([[4.6]])
    print("Distances to the 3 nearest points:", distances[0].round(2))
    print("Positions of the 3 nearest points:", positions[0])
    print("Their hours:", [hours[i][0] for i in positions[0]])


# ---------------------------------------------------------------
# PART 2: CHOOSING K AND TESTING (Programs 6 to 10)
# ---------------------------------------------------------------

def program6():
    # Try different K values
    data = [[1, 2], [2, 3], [3, 3], [4, 4], [5, 4], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 0, 1, 1, 1]
    for k in [1, 3, 5]:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(data, label)
        print("K =", k, "-> prediction for [5, 5]:", model.predict([[5, 5]])[0])


def program7():
    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    result = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    x_train, x_test, y_train, y_test = train_test_split(hours, result, test_size=0.3, random_state=1)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    print("Test accuracy:", round(model.score(x_test, y_test), 2))


def program8():
    # Confusion matrix
    from sklearn.metrics import confusion_matrix
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    predicted = [0, 0, 0, 1, 1, 1, 0, 1]
    print("Confusion matrix:")
    print(confusion_matrix(actual, predicted))


def program9():
    # Classification report
    from sklearn.metrics import classification_report
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    predicted = [0, 0, 0, 1, 1, 1, 0, 1]
    print(classification_report(actual, predicted))


def program10():
    # Different distance types
    data = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 1, 1]
    for d in ["euclidean", "manhattan"]:
        model = KNeighborsClassifier(n_neighbors=3, metric=d)
        model.fit(data, label)
        print(d, "distance prediction for [5, 5]:", model.predict([[5, 5]])[0])


# ---------------------------------------------------------------
# PART 3: DATA AND SETTINGS (Programs 11 to 15)
# ---------------------------------------------------------------

def program11():
    # Get probabilities from KNN
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    prob = model.predict_proba([[4.6]])[0][1]
    print("Chance of passing with 4.6 hours:", round(prob * 100, 1), "%")


def program12():
    # Predict for many students at once
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
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
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(df[["hours"]], df["passed"])
    print("Prediction for 6 hours:", model.predict(pd.DataFrame({"hours": [6]}))[0])


def program14():
    # Closer neighbors get more weight
    data = [[1], [2], [3], [7]]
    label = [0, 0, 0, 1]
    for w in ["uniform", "distance"]:
        model = KNeighborsClassifier(n_neighbors=4, weights=w)
        model.fit(data, label)
        print("weights =", w, "-> prediction for 6:", model.predict([[6]])[0])


def program15():
    # Plot two groups of data and a new point
    import matplotlib.pyplot as plt
    marks = [30, 35, 40, 45, 55, 60, 70, 80]
    attendance = [50, 55, 60, 65, 70, 80, 85, 90]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    colors = ["red" if r == 0 else "green" for r in result]
    plt.scatter(marks, attendance, c=colors)
    plt.scatter([50], [68], color="blue", marker="*", s=250, label="New student")
    plt.xlabel("Marks")
    plt.ylabel("Attendance %")
    plt.title("Red = Fail, Green = Pass")
    plt.legend()
    plt.show()


# ---------------------------------------------------------------
# PART 4: REAL-LIFE EXAMPLES (Programs 16 to 20)
# ---------------------------------------------------------------

def program16():
    # Fruit classification: apple or orange (weight in grams, size in cm)
    data = [[150, 7], [160, 7.5], [170, 8], [155, 7.2], [200, 9], [210, 9.5], [220, 10], [205, 9.2]]
    fruit = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, fruit)
    names = ["Apple", "Orange"]
    answer = model.predict([[195, 8.8]])[0]
    print("Fruit weighing 195 g, size 8.8 cm:", names[answer])


def program17():
    # Iris flowers (3 types)
    from sklearn.datasets import load_iris
    iris = load_iris()
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(iris.data, iris.target)
    answer = model.predict([[5.1, 3.5, 1.4, 0.2]])[0]
    print("Flower type:", iris.target_names[answer])


def program18():
    # Will the customer buy? (age and salary in thousands)
    data = [[19, 20], [22, 25], [25, 30], [30, 40], [35, 80], [40, 90], [45, 100], [50, 110]]
    buy = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, buy)
    age = float(input("Enter age: "))
    salary = float(input("Enter salary in thousands: "))
    answer = model.predict([[age, salary]])[0]
    print("Customer:", "Will buy" if answer == 1 else "Will not buy")


def program19():
    # Movie preference from age and hours of TV watched
    data = [[15, 5], [17, 6], [20, 4], [25, 3], [35, 1], [40, 2], [45, 1], [50, 1]]
    movie = [1, 1, 1, 1, 0, 0, 0, 0]   # 1 = Action, 0 = Drama
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, movie)
    answer = model.predict([[22, 4]])[0]
    print("Person aged 22 watching 4 hours:", "Likes Action" if answer == 1 else "Likes Drama")


def program20():
    # Diabetes prediction from glucose and BMI
    data = [[85, 22], [90, 24], [95, 25], [100, 27], [140, 32], [160, 35], [180, 38], [200, 40]]
    diabetes = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, diabetes)
    answer = model.predict([[150, 33]])[0]
    print("Glucose 150, BMI 33:", "Diabetic" if answer == 1 else "Not diabetic")


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
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(scaled, loan)
    new = scaler.transform([[65, 38]])
    print("Loan prediction:", "Approved" if model.predict(new)[0] == 1 else "Rejected")


def program22():
    # Cross validation
    from sklearn.model_selection import cross_val_score
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    result = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    scores = cross_val_score(KNeighborsClassifier(n_neighbors=3), hours, result, cv=3)
    print("Scores:", [round(float(s), 2) for s in scores])
    print("Average:", round(float(scores.mean()), 2))


def program23():
    # Find the best K value
    from sklearn.datasets import load_iris
    from sklearn.model_selection import cross_val_score
    iris = load_iris()
    best_k = 1
    best_score = 0
    for k in range(1, 16):
        model = KNeighborsClassifier(n_neighbors=k)
        score = cross_val_score(model, iris.data, iris.target, cv=5).mean()
        print("K =", k, "-> score:", round(float(score), 3))
        if score > best_score:
            best_score = score
            best_k = k
    print("Best K:", best_k)


def program24():
    # Breast cancer dataset (a real dataset from sklearn)
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    data = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    print("Accuracy on cancer data:", round(model.score(x_test, y_test), 2))


def program25():
    # Wine dataset (3 types of wine)
    from sklearn.datasets import load_wine
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    data = load_wine()
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=1)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)
    print("Accuracy on wine data:", round(model.score(x_test, y_test), 2))


# ---------------------------------------------------------------
# PART 6: MORE PROGRAMS (Programs 26 to 30)
# ---------------------------------------------------------------

def program26():
    # KNN Regressor: predict a number
    from sklearn.neighbors import KNeighborsRegressor
    hours = [[1], [2], [3], [4], [5], [6]]
    marks = [35, 45, 55, 65, 75, 85]
    model = KNeighborsRegressor(n_neighbors=2)
    model.fit(hours, marks)
    print("Marks for 3.5 hours:", model.predict([[3.5]])[0])


def program27():
    # Plot K value against accuracy
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)
    ks = range(1, 21)
    scores = []
    for k in ks:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        scores.append(model.score(x_test, y_test))
    plt.plot(ks, scores, marker="o")
    plt.xlabel("K value")
    plt.ylabel("Accuracy")
    plt.title("K value vs Accuracy")
    plt.show()


def program28():
    # Plot the decision area
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.array([[1, 2], [2, 3], [3, 3], [4, 4], [5, 4], [6, 5], [7, 8], [8, 6]])
    label = [0, 0, 0, 1, 0, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(data, label)
    xx, yy = np.meshgrid(np.linspace(0, 9, 200), np.linspace(0, 9, 200))
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, zz, alpha=0.3)
    plt.scatter(data[:, 0], data[:, 1], c=label, edgecolors="black")
    plt.title("KNN Decision Area (K = 3)")
    plt.show()


def program29():
    # Scaler and KNN together using a pipeline
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=3))
    model.fit(data, loan)
    answer = model.predict([[65, 38]])[0]
    print("Loan prediction:", "Approved" if answer == 1 else "Rejected")


def program30():
    # Save the model to a file and load it again
    import pickle
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(hours, result)
    with open("knn_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved as knn_model.pkl")
    with open("knn_model.pkl", "rb") as f:
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

print("30 Programs in KNN")
choice = int(input("Enter program number (1-30): "))

if choice in programs:
    print("\n--- Program", choice, "---")
    programs[choice]()
else:
    print("Please enter a number between 1 and 30.")
