1. Install requirements: `pip install -r requirements.txt`
2. Create and start containers: `docker-compose -f docker-compose.yaml up -d`
3. Check services (for remote use, replace `localhost` with the desired ip address):
    - MLflow: http://localhost:5001
    - Airflow: http://localhost:8081 (user: `airflow`, password: `airflow`)
    - JupyterLab: http://localhost:8889 (token:`docker`)
    - Minio: http://localhost:9001 (user: `minioadmin`, password: `minioadmin`)
4. Run `mlflow_test` DAG in Airflow (optionally, you can look at DAG code in `dags/dag_test.py` and
   study `mlflow_test.py` in the `dags/src` folder).
5. Check the results in MLflow (and optionally in Minio).