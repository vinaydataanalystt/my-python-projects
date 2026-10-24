

from sklearn.svm import SVC


# ---------------------------------------------------------------
# PART 1: BASIC SVM (Programs 1 to 5)
# ---------------------------------------------------------------

def program1():
    # Predict Pass (1) or Fail (0) from study hours
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(hours, result)
    answer = model.predict([[5.5]])[0]
    print("Result for 5.5 hours:", "Pass" if answer == 1 else "Fail")


def program2():
    # Predict for two inputs: hours studied and attendance
    data = [[1, 50], [2, 55], [3, 60], [4, 65], [5, 75], [6, 80], [7, 85], [8, 90]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, result)
    answer = model.predict([[5, 70]])[0]
    print("5 hours, 70% attendance:", "Pass" if answer == 1 else "Fail")


def program3():
    # Pass or Fail from user input
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(hours, result)
    h = float(input("Enter study hours: "))
    answer = model.predict([[h]])[0]
    print("Prediction:", "Pass" if answer == 1 else "Fail")


def program4():
    # Check the accuracy of the model
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(hours, result)
    print("Accuracy:", model.score(hours, result))


def program5():
    # Plot the data with the SVM dividing line
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.array([[1, 50], [2, 55], [3, 60], [4, 65], [5, 75], [6, 80], [7, 85], [8, 90]])
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, result)
    w = model.coef_[0]
    b = model.intercept_[0]
    x = np.linspace(0, 9, 50)
    y = -(w[0] * x + b) / w[1]
    colors = ["red" if r == 0 else "green" for r in result]
    plt.scatter(data[:, 0], data[:, 1], c=colors)
    plt.plot(x, y, color="black")
    plt.ylim(40, 100)
    plt.xlabel("Hours studied")
    plt.ylabel("Attendance %")
    plt.title("SVM line (Red = Fail, Green = Pass)")
    plt.show()


# ---------------------------------------------------------------
# PART 2: KERNELS AND SUPPORT VECTORS (Programs 6 to 10)
# ---------------------------------------------------------------

def program6():
    # Linear kernel
    data = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, label)
    print("Linear kernel prediction for [5, 5]:", model.predict([[5, 5]])[0])


def program7():
    # RBF kernel
    data = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 1, 1]
    model = SVC(kernel="rbf")
    model.fit(data, label)
    print("RBF kernel prediction for [5, 5]:", model.predict([[5, 5]])[0])


def program8():
    # Polynomial kernel
    data = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 1, 1]
    model = SVC(kernel="poly", degree=3)
    model.fit(data, label)
    print("Poly kernel prediction for [5, 5]:", model.predict([[5, 5]])[0])


def program9():
    # Show the support vectors (the points that decide the line)
    data = [[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, label)
    print("Support vectors:")
    print(model.support_vectors_)
    print("Number of support vectors for each class:", model.n_support_)


def program10():
    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    result = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    x_train, x_test, y_train, y_test = train_test_split(hours, result, test_size=0.3, random_state=1)
    model = SVC(kernel="linear")
    model.fit(x_train, y_train)
    print("Test accuracy:", round(model.score(x_test, y_test), 2))


# ---------------------------------------------------------------
# PART 3: METRICS AND SETTINGS (Programs 11 to 15)
# ---------------------------------------------------------------

def program11():
    # Confusion matrix
    from sklearn.metrics import confusion_matrix
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    predicted = [0, 0, 0, 1, 1, 1, 0, 1]
    print("Confusion matrix:")
    print(confusion_matrix(actual, predicted))


def program12():
    # Classification report
    from sklearn.metrics import classification_report
    actual = [0, 0, 0, 0, 1, 1, 1, 1]
    predicted = [0, 0, 0, 1, 1, 1, 0, 1]
    print(classification_report(actual, predicted))


def program13():
    # Get probabilities from SVM
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear", probability=True, random_state=1)
    model.fit(hours, result)
    prob = model.predict_proba([[5]])[0][1]
    print("Chance of passing with 5 hours:", round(prob * 100, 1), "%")


def program14():
    # Effect of the C value
    data = [[1, 2], [2, 3], [3, 3], [4, 4], [5, 4], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 0, 1, 1, 1]
    for c in [0.1, 1, 100]:
        model = SVC(kernel="linear", C=c)
        model.fit(data, label)
        print("C =", c, "-> accuracy:", model.score(data, label), "-> support vectors:", len(model.support_vectors_))


def program15():
    # Effect of the gamma value (RBF kernel)
    data = [[1, 2], [2, 3], [3, 3], [4, 4], [5, 4], [6, 5], [7, 8], [8, 6]]
    label = [0, 0, 0, 1, 0, 1, 1, 1]
    for g in [0.01, 0.1, 1, 10]:
        model = SVC(kernel="rbf", gamma=g)
        model.fit(data, label)
        print("gamma =", g, "-> accuracy:", model.score(data, label))


# ---------------------------------------------------------------
# PART 4: REAL-LIFE EXAMPLES (Programs 16 to 20)
# ---------------------------------------------------------------

def program16():
    # Spam detection from number of links and capital words
    data = [[0, 1], [1, 2], [0, 0], [5, 8], [7, 10], [6, 9], [1, 1], [8, 12]]
    spam = [0, 0, 0, 1, 1, 1, 0, 1]
    model = SVC(kernel="linear")
    model.fit(data, spam)
    answer = model.predict([[6, 7]])[0]
    print("Email with 6 links and 7 capital words:", "Spam" if answer == 1 else "Not spam")


def program17():
    # Diabetes prediction from glucose and BMI
    data = [[85, 22], [90, 24], [95, 25], [100, 27], [140, 32], [160, 35], [180, 38], [200, 40]]
    diabetes = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, diabetes)
    answer = model.predict([[150, 33]])[0]
    print("Glucose 150, BMI 33:", "Diabetic" if answer == 1 else "Not diabetic")


def program18():
    # Fruit classification: apple or orange (weight in grams, size in cm)
    data = [[150, 7], [160, 7.5], [170, 8], [155, 7.2], [200, 9], [210, 9.5], [220, 10], [205, 9.2]]
    fruit = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(data, fruit)
    names = ["Apple", "Orange"]
    answer = model.predict([[195, 8.8]])[0]
    print("Fruit weighing 195 g, size 8.8 cm:", names[answer])


def program19():
    # Loan approval from salary and age
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]   # salary in thousands
    model = SVC(kernel="linear")
    model.fit(data, loan)
    s = float(input("Enter salary in thousands: "))
    a = float(input("Enter age: "))
    answer = model.predict([[s, a]])[0]
    print("Loan:", "Approved" if answer == 1 else "Rejected")


def program20():
    # Iris flowers (3 types) with SVM
    from sklearn.datasets import load_iris
    iris = load_iris()
    model = SVC(kernel="linear")
    model.fit(iris.data, iris.target)
    answer = model.predict([[5.1, 3.5, 1.4, 0.2]])[0]
    print("Flower type:", iris.target_names[answer])


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
    model = SVC(kernel="rbf")
    model.fit(scaled, loan)
    new = scaler.transform([[65, 38]])
    print("Loan prediction:", "Approved" if model.predict(new)[0] == 1 else "Rejected")


def program22():
    # Cross validation
    from sklearn.model_selection import cross_val_score
    hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    result = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    scores = cross_val_score(SVC(kernel="linear"), hours, result, cv=3)
    print("Scores:", [round(float(s), 2) for s in scores])
    print("Average:", round(float(scores.mean()), 2))


def program23():
    # Find the best settings with GridSearchCV
    from sklearn.datasets import load_iris
    from sklearn.model_selection import GridSearchCV
    iris = load_iris()
    settings = {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}
    search = GridSearchCV(SVC(), settings, cv=5)
    search.fit(iris.data, iris.target)
    print("Best settings:", search.best_params_)
    print("Best score:", round(search.best_score_, 2))


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
    model = SVC(kernel="rbf")
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
    model = SVC(kernel="rbf")
    model.fit(x_train, y_train)
    print("Accuracy on wine data:", round(model.score(x_test, y_test), 2))


# ---------------------------------------------------------------
# PART 6: MORE PROGRAMS (Programs 26 to 30)
# ---------------------------------------------------------------

def program26():
    # SVR: SVM for predicting numbers
    from sklearn.svm import SVR
    hours = [[1], [2], [3], [4], [5], [6]]
    marks = [35, 45, 55, 65, 75, 85]
    model = SVR(kernel="linear", C=100)
    model.fit(hours, marks)
    print("Marks for 7 hours:", round(model.predict([[7]])[0], 1))


def program27():
    # Plot the decision area with the RBF kernel
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.array([[1, 2], [2, 3], [3, 3], [4, 4], [5, 4], [6, 5], [7, 8], [8, 6]])
    label = [0, 0, 0, 1, 0, 1, 1, 1]
    model = SVC(kernel="rbf", gamma=0.2)
    model.fit(data, label)
    xx, yy = np.meshgrid(np.linspace(0, 9, 200), np.linspace(0, 9, 200))
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    plt.contourf(xx, yy, zz, alpha=0.3)
    plt.scatter(data[:, 0], data[:, 1], c=label, edgecolors="black")
    plt.title("SVM Decision Area (RBF)")
    plt.show()


def program28():
    # Compare all kernels
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)
    for k in ["linear", "rbf", "poly", "sigmoid"]:
        model = SVC(kernel=k)
        model.fit(x_train, y_train)
        print(k, "kernel accuracy:", round(model.score(x_test, y_test), 2))


def program29():
    # Scaler and SVM together using a pipeline
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    data = [[20, 22], [25, 24], [30, 28], [40, 35], [60, 40], [70, 45], [80, 50], [90, 52]]
    loan = [0, 0, 0, 0, 1, 1, 1, 1]
    model = make_pipeline(StandardScaler(), SVC(kernel="rbf"))
    model.fit(data, loan)
    answer = model.predict([[65, 38]])[0]
    print("Loan prediction:", "Approved" if answer == 1 else "Rejected")


def program30():
    # Save the model to a file and load it again
    import pickle
    hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
    result = [0, 0, 0, 0, 1, 1, 1, 1]
    model = SVC(kernel="linear")
    model.fit(hours, result)
    with open("svm_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved as svm_model.pkl")
    with open("svm_model.pkl", "rb") as f:
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

print("30 Programs in SVM")
choice = int(input("Enter program number (1-30): "))

if choice in programs:
    print("\n--- Program", choice, "---")
    programs[choice]()
else:
    print("Please enter a number between 1 and 30.")
