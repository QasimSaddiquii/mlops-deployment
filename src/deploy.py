import mlflow
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
mlflow.set_tracking_uri("http://localhost:5000")

# Champion model load karega
model = mlflow.pyfunc.load_model("models:/Iris_RF_Model@Champion")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
