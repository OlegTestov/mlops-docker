import os
from random import random

import lightgbm as lgb

import mlflow
import pandas as pd


def mlflow_test_func():
    os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = f"http://minio:9000"

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("test_experiment")

    with mlflow.start_run() as mlflow_run:
        # Log a parameter (key-value pair)
        mlflow.log_param("foo", "bar")

        # Log a metric
        mlflow.log_metric("hello_metric", random())

        # Log an artifact (output file)
        os.system(f"echo 'hello world' > helloworld.txt")
        mlflow.log_artifact("helloworld.txt")
        os.remove("helloworld.txt")

        # Log a model (xgboost model)
        df = pd.DataFrame({'X': [1, 2, 3], 'y': [1, 2, 3]})
        dtrain = lgb.Dataset(df[['X']], label=df['y'])
        params = {
            'objective': 'regression',
        }
        model = lgb.train(params, dtrain)
        mlflow.lightgbm.log_model(model, "lightgbm-model")
