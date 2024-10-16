from airflow import DAG
from scripts.custom_operator import CustomOperator
from datetime import datetime


with DAG(dag_id='custom_operator', description='testing custom operators', start_date=datetime(2024, 10, 15)) as dag:

    t1 = CustomOperator(task_id='Custom_operator', name='Juan')
