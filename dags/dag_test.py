# DAG definition
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from src import custom_sum

dag = DAG(
    "data_pipeline",
    schedule_interval="0 * * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False
)


# Functions definition
def extract_data_func():
    res = custom_sum(1, 2)
    print("Extracting data", res)


def transform_data_func():
    print("Transforming data")


def load_data_func():
    print("Loading data")


# Tasks definition
extract_data = PythonOperator(
    task_id="extract_data",
    python_callable=extract_data_func,
    dag=dag
)

transform_data = PythonOperator(
    task_id="transform_data",
    python_callable=transform_data_func,
    dag=dag
)

load_data = PythonOperator(
    task_id="load_data",
    python_callable=load_data_func,
    dag=dag
)

# Task dependencies
extract_data >> transform_data >> load_data
