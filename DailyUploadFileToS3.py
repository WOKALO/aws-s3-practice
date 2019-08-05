"""
Upload a file to s3 bucket scheduled daily
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args={
	'owner':'airflow',
	'depends_on_past': False,
	'start_date': datetime(2019,7,28),
	#'email':['airflow@exmaple.com'],
	#'email_on_failure': True,
	#'email_on_retry': True,
	'retries': 0,
	'retry_delay': timedelta(minutes=5),
	'schedule_interval':'@once',
}

testDag = DAG('Upload_housingprice',default_args=default_args, schedule_interval=timedelta(days=1))

#t1: use bashoperator call API

upload_singleFile_s3 = BashOperator(
	task_id = 'upload_ex2data',
	bash_command = '/home/lzgtk/Python\ Projects/Dataflow/upload_one_file_to_s3.sh ',
	dag = testDag,
)

sleep5 = BashOperator(
	task_id = 'sleep',
	bash_command= 'sleep 5',
	dag = testDag,
)


