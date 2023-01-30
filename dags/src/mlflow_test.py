import os

import xgboost as xgb
import mlflow
import pandas as pd

os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = f"http://localhost:9000"

mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("test_experiment")

mlflow.start_run()

# Log a parameter (key-value pair)
mlflow.log_param("foo", "bar")

# Log an artifact (output file)
with open("output.txt", "w") as f:
    f.write("Hello world!")
mlflow.log_artifact("output.txt")
os.remove("output.txt")

# Log a model (xgboost model)
df = pd.DataFrame({'X': [1, 2, 3], 'y': [1, 2, 3]})
dtrain = xgb.DMatrix(df[['X']], label=df['y'])
params = {
    'objective': 'reg:squarederror'
}
model = xgb.train(params, dtrain)
mlflow.xgboost.log_model(model, "xgboost_model")

mlflow.end_run()
