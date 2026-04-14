import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Iris_Classification")

df = pd.read_csv('data/iris.csv')
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run() as run:
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    mlflow.sklearn.log_model(model, "model")
    
    # Register Model and assign Challenger alias
    client = MlflowClient()
    model_name = "Iris_RF_Model"
    model_version = mlflow.register_model(f"runs:/{run.info.run_id}/model", model_name)
    client.set_registered_model_alias(model_name, "Challenger", model_version.version)
    print("Model trained and registered as Challenger")
