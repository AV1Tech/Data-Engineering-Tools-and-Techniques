from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print('Hello world!')

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(task_id='start', dag=dag)
hello_task = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> hello_task >> end
