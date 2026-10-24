# Instructions to build the app container
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Train the model inside the container
RUN python train_model.py

# Cloud Run gives the port in the PORT variable
CMD exec gunicorn --bind 0.0.0.0:${PORT:-8080} app:app
