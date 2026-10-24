

from sklearn.linear_model import LinearRegression


# ---------------------------------------------------------------
# PART 1: SIMPLE LINEAR REGRESSION (Programs 1 to 5)
# ---------------------------------------------------------------

def program1():
    # Predict marks from study hours
    hours = [[1], [2], [3], [4], [5]]
    marks = [35, 45, 55, 65, 75]
    model = LinearRegression()
    model.fit(hours, marks)
    print("Marks for 6 hours:", round(model.predict([[6]])[0], 2))


def program2():
    # Show slope and intercept
    hours = [[1], [2], [3], [4], [5]]
    marks = [35, 45, 55, 65, 75]
    model = LinearRegression()
    model.fit(hours, marks)
    print("Slope:", round(model.coef_[0], 2))
    print("Intercept:", round(model.intercept_, 2))


def program3():
    # Predict salary from experience (user input)
    years = [[1], [2], [3], [4], [5]]
    salary = [30000, 35000, 40000, 45000, 50000]
    model = LinearRegression()
    model.fit(years, salary)
    exp = float(input("Enter years of experience: "))
    print("Predicted salary:", round(model.predict([[exp]])[0]))


def program4():
    # Plot the regression line
    import matplotlib.pyplot as plt
    hours = [[1], [2], [3], [4], [5]]
    marks = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(hours, marks)
    plt.scatter(hours, marks)
    plt.plot(hours, model.predict(hours), color="red")
    plt.xlabel("Hours studied")
    plt.ylabel("Marks")
    plt.title("Study Hours vs Marks")
    plt.show()


def program5():
    # R2 score: how good is the model
    hours = [[1], [2], [3], [4], [5]]
    marks = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(hours, marks)
    print("R2 score:", round(model.score(hours, marks), 2))


# ---------------------------------------------------------------
# PART 2: MULTIPLE LINEAR REGRESSION (Programs 6 to 10)
# ---------------------------------------------------------------

def program6():
    # House price from area and bedrooms
    data = [[1000, 2], [1500, 3], [1800, 3], [2400, 4], [3000, 5]]
    price = [50, 70, 80, 110, 140]   # in lakhs
    model = LinearRegression()
    model.fit(data, price)
    print("Price for 2000 sqft, 3 bedrooms:", round(model.predict([[2000, 3]])[0], 2), "lakhs")


def program7():
    # Coefficients of multiple regression
    data = [[1000, 2], [1500, 3], [1800, 3], [2400, 4], [3000, 5]]
    price = [50, 70, 80, 110, 140]
    model = LinearRegression()
    model.fit(data, price)
    print("Area coefficient:", round(model.coef_[0], 4))
    print("Bedroom coefficient:", round(model.coef_[1], 4))
    print("Intercept:", round(model.intercept_, 2))


def program8():
    # Split data into training and testing
    from sklearn.model_selection import train_test_split
    x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    y = [12, 24, 33, 47, 52, 66, 71, 85, 91, 105]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    model = LinearRegression()
    model.fit(x_train, y_train)
    print("Test score:", round(model.score(x_test, y_test), 2))


def program9():
    # Mean Squared Error and Mean Absolute Error
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(x, y)
    pred = model.predict(x)
    print("MSE:", round(mean_squared_error(y, pred), 2))
    print("MAE:", round(mean_absolute_error(y, pred), 2))


def program10():
    # Root Mean Squared Error
    from sklearn.metrics import mean_squared_error
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(x, y)
    pred = model.predict(x)
    rmse = mean_squared_error(y, pred) ** 0.5
    print("RMSE:", round(rmse, 2))


# ---------------------------------------------------------------
# PART 3: WORKING WITH DATA (Programs 11 to 15)
# ---------------------------------------------------------------

def program11():
    # Use a pandas table (DataFrame)
    import pandas as pd
    df = pd.DataFrame({
        "hours": [1, 2, 3, 4, 5],
        "marks": [35, 48, 52, 68, 74],
    })
    print(df)
    model = LinearRegression()
    model.fit(df[["hours"]], df["marks"])
    print("Prediction for 7 hours:", round(model.predict(pd.DataFrame({"hours": [7]}))[0], 2))


def program12():
    # Predict many values at once
    x = [[1], [2], [3], [4], [5]]
    y = [35, 45, 55, 65, 75]
    model = LinearRegression()
    model.fit(x, y)
    new_hours = [[6], [7], [8]]
    result = model.predict(new_hours)
    for h, r in zip(new_hours, result):
        print("Hours:", h[0], "-> Marks:", round(r, 2))


def program13():
    # Residuals (actual minus predicted)
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(x, y)
    pred = model.predict(x)
    for i in range(len(y)):
        print("Actual:", y[i], "Predicted:", round(pred[i], 2), "Residual:", round(y[i] - pred[i], 2))


def program14():
    # House price from area (user input)
    area = [[800], [1000], [1200], [1500], [2000]]
    price = [40, 52, 61, 78, 102]
    model = LinearRegression()
    model.fit(area, price)
    a = float(input("Enter house area in sqft: "))
    print("Predicted price:", round(model.predict([[a]])[0], 2), "lakhs")


def program15():
    # Plot with a predicted point
    import matplotlib.pyplot as plt
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(x, y)
    plt.scatter(x, y, label="Data")
    plt.plot(x, model.predict(x), color="red", label="Line")
    plt.scatter([[6]], model.predict([[6]]), color="green", label="Prediction (6 hours)")
    plt.legend()
    plt.title("Prediction on the line")
    plt.show()


# ---------------------------------------------------------------
# PART 4: REAL-LIFE EXAMPLES (Programs 16 to 20)
# ---------------------------------------------------------------

def program16():
    # Used car price from age
    age = [[1], [2], [3], [4], [5]]
    price = [8, 7, 6.2, 5.1, 4.3]   # in lakhs
    model = LinearRegression()
    model.fit(age, price)
    print("Price of a 6 year old car:", round(model.predict([[6]])[0], 2), "lakhs")


def program17():
    # Ice cream sales from temperature
    temp = [[20], [25], [30], [35], [40]]
    sales = [100, 150, 210, 260, 320]
    model = LinearRegression()
    model.fit(temp, sales)
    print("Sales at 33 degrees:", round(model.predict([[33]])[0]))


def program18():
    # Slope and intercept using the formula (no library model)
    x = [1, 2, 3, 4, 5]
    y = [35, 48, 52, 68, 74]
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    top = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    bottom = sum((x[i] - mean_x) ** 2 for i in range(n))
    slope = top / bottom
    intercept = mean_y - slope * mean_x
    print("Slope:", round(slope, 2))
    print("Intercept:", round(intercept, 2))


def program19():
    # Linear regression using numpy polyfit
    import numpy as np
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([35, 48, 52, 68, 74])
    slope, intercept = np.polyfit(x, y, 1)
    print("Slope:", round(slope, 2))
    print("Intercept:", round(intercept, 2))


def program20():
    # Polynomial regression (curved line)
    from sklearn.preprocessing import PolynomialFeatures
    x = [[1], [2], [3], [4], [5]]
    y = [2, 8, 18, 32, 50]
    poly = PolynomialFeatures(degree=2)
    x_poly = poly.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    print("Prediction for 6:", round(model.predict(poly.transform([[6]]))[0], 2))


# ---------------------------------------------------------------
# PART 5: IMPROVING THE MODEL (Programs 21 to 25)
# ---------------------------------------------------------------

def program21():
    # Ridge regression
    from sklearn.linear_model import Ridge
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = Ridge(alpha=1.0)
    model.fit(x, y)
    print("Ridge prediction for 6:", round(model.predict([[6]])[0], 2))


def program22():
    # Lasso regression
    from sklearn.linear_model import Lasso
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = Lasso(alpha=0.1)
    model.fit(x, y)
    print("Lasso prediction for 6:", round(model.predict([[6]])[0], 2))


def program23():
    # Feature scaling
    from sklearn.preprocessing import StandardScaler
    x = [[1000, 2], [1500, 3], [1800, 3], [2400, 4], [3000, 5]]
    y = [50, 70, 80, 110, 140]
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    model = LinearRegression()
    model.fit(x_scaled, y)
    new = scaler.transform([[2000, 3]])
    print("Prediction for 2000 sqft, 3 bedrooms:", round(model.predict(new)[0], 2))


def program24():
    # Cross validation
    from sklearn.model_selection import cross_val_score
    x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    y = [12, 24, 33, 47, 52, 66, 71, 85, 91, 105]
    scores = cross_val_score(LinearRegression(), x, y, cv=3)
    print("Scores:", [round(float(s), 2) for s in scores])
    print("Average score:", round(scores.mean(), 2))


def program25():
    # Actual vs predicted graph
    import matplotlib.pyplot as plt
    x = [[1], [2], [3], [4], [5], [6]]
    y = [12, 24, 33, 47, 52, 66]
    model = LinearRegression()
    model.fit(x, y)
    pred = model.predict(x)
    plt.scatter(y, pred)
    plt.plot([min(y), max(y)], [min(y), max(y)], color="red")
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted")
    plt.show()


# ---------------------------------------------------------------
# PART 6: MORE PROGRAMS (Programs 26 to 30)
# ---------------------------------------------------------------

def program26():
    # Salary from experience and age
    data = [[1, 22], [2, 24], [3, 26], [5, 29], [8, 33]]
    salary = [25000, 32000, 40000, 55000, 80000]
    model = LinearRegression()
    model.fit(data, salary)
    print("Salary for 4 years experience, age 27:", round(model.predict([[4, 27]])[0]))


def program27():
    # Mileage of a car from engine size
    engine = [[1.0], [1.2], [1.5], [2.0], [2.5]]
    mileage = [24, 22, 19, 15, 12]
    model = LinearRegression()
    model.fit(engine, mileage)
    print("Mileage for 1.8 engine:", round(model.predict([[1.8]])[0], 2), "km/l")


def program28():
    # Show the equation y = m x + c
    x = [[1], [2], [3], [4], [5]]
    y = [35, 45, 55, 65, 75]
    model = LinearRegression()
    model.fit(x, y)
    m = round(model.coef_[0], 2)
    c = round(model.intercept_, 2)
    print("Equation: y =", m, "* x +", c)


def program29():
    # Residual plot
    import matplotlib.pyplot as plt
    x = [[1], [2], [3], [4], [5]]
    y = [35, 48, 52, 68, 74]
    model = LinearRegression()
    model.fit(x, y)
    residuals = y - model.predict(x)
    plt.scatter(model.predict(x), residuals)
    plt.axhline(0, color="red")
    plt.xlabel("Predicted")
    plt.ylabel("Residual")
    plt.title("Residual Plot")
    plt.show()


def program30():
    # Save the model to a file and load it again
    import pickle
    x = [[1], [2], [3], [4], [5]]
    y = [35, 45, 55, 65, 75]
    model = LinearRegression()
    model.fit(x, y)
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model saved as model.pkl")
    with open("model.pkl", "rb") as f:
        loaded = pickle.load(f)
    print("Loaded model prediction for 6:", round(loaded.predict([[6]])[0], 2))


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

print("30 Programs in Linear Regression")
choice = int(input("Enter program number (1-30): "))

if choice in programs:
    print("\n--- Program", choice, "---")
    programs[choice]()
else:
    print("Please enter a number between 1 and 30.")