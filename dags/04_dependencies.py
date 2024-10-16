from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from scripts.helloworld import hello
from datetime import datetime


with DAG(dag_id='dependencies', description="Using task dependencies", start_date=datetime(2024, 10, 15)) as dag:

    t1 = PythonOperator(task_id='tarea1',
                        python_callable=hello)

    t2 = BashOperator(task_id='tarea2', bash_command='echo "Tarea 2')

    t3 = BashOperator(task_id='tarea3', bash_command='echo "Tarea 3')

    t4 = BashOperator(task_id='tarea4', bash_command='echo "Tarea 4')

    t1 >> t2 >> [t3, t4]

#    t1.set_downstream(t2)
#    t2.set_downstream([t3, t4])
