import mlflow
import pandas as pd

# MLflow server ka URL set karein
mlflow.set_tracking_uri("http://localhost:5000")

model_name = "Iris_RF_Model"
alias = "Challenger-pre-test"

try:
    print(f"Loading model '{model_name}' with alias '{alias}'...")
    # Alias ke zariye model load karein
    model_uri = f"models:/{model_name}@{alias}"
    model = mlflow.pyfunc.load_model(model_uri)

    # Test ke liye ek dummy record banayen (Iris dataset format)
    test_data = pd.DataFrame(
        [[5.1, 3.5, 1.4, 0.2]], 
        columns=["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
    )

    # Model se prediction karwayen
    prediction = model.predict(test_data)
    
    print(f"Prediction successful! Output: {prediction}")
    print("Model Test Passed Successfully! ✅")

except Exception as e:
    print(f"Model testing failed! Error: {e}")
    exit(1) # Agar error aaye toh Jenkins pipeline fail ho jaye
