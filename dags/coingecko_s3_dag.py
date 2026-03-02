from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dags.coingecko_to_s3 import fetch_and_upload

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='coingecko_to_s3_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='fetch_and_upload_crypto_data',
        python_callable=fetch_and_upload
    )

    task