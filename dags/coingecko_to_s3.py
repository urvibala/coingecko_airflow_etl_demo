import requests
import boto3
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# AWS Credentials
AWS_ACCESS_KEY = os.getenv("access_key")
AWS_SECRET_KEY = os.getenv("secret_key")
BUCKET_NAME = os.getenv("bucket_name")

def fetch_and_upload():

    # 1. Fetch data from CoinGecko
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    # 2. Convert to JSON string
    json_data = json.dumps(data)

    # 3. Upload to S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    filename = f"crypto_data_{datetime.now().date()}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json_data
    )

    print("Upload successful!")
