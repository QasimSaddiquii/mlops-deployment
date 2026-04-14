import sys
from mlflow.tracking import MlflowClient

client = MlflowClient(tracking_uri="http://localhost:5000")
model_name = "Iris_RF_Model"
old_alias = sys.argv[1]
new_alias = sys.argv[2]

try:
    version = client.get_model_version_by_alias(model_name, old_alias).version
    client.set_registered_model_alias(model_name, new_alias, version)
    print(f"Updated alias from {old_alias} to {new_alias}")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
