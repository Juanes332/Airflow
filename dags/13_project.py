from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from scripts.generate_platzi_data import _generate_platzi_data

from datetime import datetime


with DAG(dag_id="space",
         description="info satelite",
         schedule_interval="@daily",
         start_date=datetime(2022, 8, 20),
         end_date=datetime(2022, 8, 25),
         max_active_runs=1) as dag:

    t1 = BashOperator(task_id='NASA_Confirmation',
                      bash_command='sleep 20 && echo "OK" >/tmp/response_{{ds_nodash}}.txt')

    tsensort1 = FileSensor(task_id="waiting_nasa_file",
                           filepath="/tmp/response_{{ds_nodash}}.txt")

    t2 = BashOperator(task_id='Spacex_Data',
                      bash_command="curl -o /tmp/history.json -L'https://api.spacexdata.com/v4/history'")

    t3 = PythonOperator(task_id='Satelite_Response',
                        python_callable=_generate_platzi_data)

    t4 = BashOperator(task_id='visualize_data',
                      bash_command='ls /tmp && head /tmp/platzi_data_{{ds_nodash}}.csv')

    t1 >> tsensort1 >> t2 >> t3 >> t4
