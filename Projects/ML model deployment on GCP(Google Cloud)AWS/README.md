# ML Model Deployment on Google Cloud

An iris flower classifier (scikit-learn) served with Flask and deployed on Google Cloud Run.

## Files
- train_model.py - trains and saves the model
- app.py - Flask web page and /predict API
- Dockerfile - packages the app into a container
- requirements.txt - Python libraries

## Run Locally
```
pip install -r requirements.txt
python train_model.py
python app.py
```
Open http://localhost:8080

## Deploy on Google Cloud Run
```
gcloud run deploy iris-predictor --source . --region asia-south1 --allow-unauthenticated
```

## API Example
POST /predict with JSON:
{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}

## Live App
(paste your Cloud Run link here)
