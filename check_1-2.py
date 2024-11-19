from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.utils.task_group import TaskGroup
from datetime import datetime

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "airflow"
}


with DAG(
    dag_id="Sprin4_Task1",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
    ) as dag:
 
    # Вам необходимо заполнить только эту секцию с сенсором
    with TaskGroup(group_id='group1') as fg1:
        f1 = FileSensor(task_id="waiting_for_file_customer_research", fs_conn_id="fs_local", filepath=str(datetime.now().date())+ "_" + "_customer_research.csv", poke_interval=5)
        f2 = FileSensor(task_id="waiting_for_file_user_order_log", fs_conn_id="fs_local", filepath=str(datetime.now().date())+ "_" + "user_order_log.csv", poke_interval=5)
        f3 = FileSensor(task_id="waiting_for_file_user_activity_log", fs_conn_id="fs_local", filepath=str(datetime.now().date())+ "_" + "user_activity_log.csv", poke_interval=5)

    fg1

