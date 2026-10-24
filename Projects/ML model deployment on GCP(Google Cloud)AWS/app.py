# Flask app that serves the ML model
# Run locally:  python app.py
import os
import joblib
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Load the saved model
folder = os.path.dirname(os.path.abspath(__file__))
saved = joblib.load(os.path.join(folder, "model.pkl"))
model = saved["model"]
names = saved["names"]

# Simple web page with a form
PAGE = """
<!DOCTYPE html>
<html>
<head><title>Iris Flower Predictor</title></head>
<body style="font-family: Arial; max-width: 450px; margin: 40px auto;">
  <h2>🌸 Iris Flower Predictor</h2>
  <form method="post" action="/">
    Sepal length (cm): <input name="sl" value="5.1"><br><br>
    Sepal width (cm): <input name="sw" value="3.5"><br><br>
    Petal length (cm): <input name="pl" value="1.4"><br><br>
    Petal width (cm): <input name="pw" value="0.2"><br><br>
    <button type="submit">Predict</button>
  </form>
  {% if result %}<h3>Prediction: {{ result }}</h3>{% endif %}
  {% if error %}<p style="color:red">{{ error }}</p>{% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result, error = None, None
    if request.method == "POST":
        try:
            values = [float(request.form[k]) for k in ["sl", "sw", "pl", "pw"]]
            result = names[model.predict([values])[0]]
        except ValueError:
            error = "Please enter numbers only."
    return render_template_string(PAGE, result=result, error=error)


# API endpoint: send JSON, get JSON back
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    values = [data["sepal_length"], data["sepal_width"],
              data["petal_length"], data["petal_width"]]
    prediction = names[model.predict([values])[0]]
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
