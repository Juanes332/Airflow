from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime


# Context Manager
with DAG(dag_id="first_dag", description="first dag description", start_date=datetime(2024, 10, 1), schedule_interval="@once") as dag:
    t1 = EmptyOperator(task_id='dummy')


# Standard constructor
dag2 = DAG(
    dag_id="dag2",
    description="2dag2",
    start_date=datetime(2024, 10, 31),
    schedule_interval="@once",
)
op2 = EmptyOperator(task_id="dummy2", dag=dag2)
