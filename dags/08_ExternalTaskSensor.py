from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor


with DAG(dag_id="externalTaskSensor",
         description="DAG Secundario",
         schedule_interval="@daily",
         start_date=datetime(2022, 8, 20),
         end_date=datetime(2022, 8, 25),
         max_active_runs=1
         ) as dag:

    t1 = ExternalTaskSensor(task_id="waiting_dag",
                            external_dag_id="externalTaskSensorScript",
                            external_task_id="tarea_bash",
                            poke_interval=10  # Cada 10 segundos pregunta si ya termino la tarea
                            )

    t2 = BashOperator(task_id="tarea_2",
                      bash_command="sleep 10 && echo 'DAG 2 finalizado!'",
                      depends_on_past=True)

    t1 >> t2
