from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id='orquestation3',
         description='testing orquestation',
         schedule_interval='@monthly',
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 6, 1),
         ) as dag:

    t1 = EmptyOperator(task_id='tarea_1')

    t2 = EmptyOperator(task_id='tarea_2')

    t3 = EmptyOperator(task_id='tarea_3')

    t4 = EmptyOperator(task_id='tarea_4')

    t1 >> t2 >> [t3, t4]
