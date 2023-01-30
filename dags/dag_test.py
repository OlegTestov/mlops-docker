# DAG definition
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from src import mlflow_test_func

dag = DAG(
    "mlflow_test",
    schedule_interval="0 * * * *",
    start_date=datetime(2022, 1, 1),
    catchup=False
)

start = DummyOperator(task_id="start", dag=dag)

mlflow_test = PythonOperator(
    task_id="mlflow_test",
    python_callable=mlflow_test_func,
    dag=dag
)

end = DummyOperator(task_id="end", dag=dag)

start >> mlflow_test >> end

