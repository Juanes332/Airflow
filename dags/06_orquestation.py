from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='orquestation',
         description='testing orquestation',
         schedule_interval='@daily',
         start_date=datetime(2024, 5, 1),
         end_date=datetime(2024, 6, 1),
         default_args={"depends_on_past": True},
         max_active_runs=1
         ) as dag:

    t1 = BashOperator(task_id='tarea_1',
                      bash_command="sleep 2 && echo 'Tarea1'")

    t2 = BashOperator(task_id='tarea_2',
                      bash_command="sleep 2 && echo 'Tarea2'")

    t3 = BashOperator(task_id='tarea_3',
                      bash_command="sleep 2 && echo 'Tarea3'")

    t4 = BashOperator(task_id='tarea_4',
                      bash_command="sleep 2 && echo 'Tarea4'")

    t1 >> t2 >> [t3, t4]
