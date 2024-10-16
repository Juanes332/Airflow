from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.helloworld import hello
from datetime import datetime


with DAG(dag_id='python_operator', description="Using Python operator", start_date=datetime(2024, 10, 15)) as dag:

    t1 = PythonOperator(task_id='hello_with_python',
                        python_callable=hello)
