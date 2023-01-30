import boto3
import os

# Run mlflow_test_func() from mlflow_test.py first to upload the helloworld.txt to S3

os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"

s3 = boto3.resource('s3', endpoint_url='http://localhost:9000')
for obj in s3.Bucket('mlflow').objects.all():
    print(obj.key)
