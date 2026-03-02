# CoinGecko Airflow ETL

A simple ETL pipeline built with Apache Airflow that fetches cryptocurrency market data from the CoinGecko API and uploads it to AWS S3.

## Tech Stack

- Python  
- Apache Airflow  
- AWS S3  
- Boto3  
- Requests  

## How It Works

1. Airflow scheduler runs the DAG daily.
2. The DAG executes a Python function.
3. Crypto market data is fetched from the CoinGecko API.
4. Data is uploaded to an AWS S3 bucket as JSON.

## Run Locally

```bash
pip install -r requirements.txt
airflow standalone
