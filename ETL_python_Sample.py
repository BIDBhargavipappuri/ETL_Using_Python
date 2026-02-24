import base64
import requests
import json
import pandas as pd
import pyodbc
from datetime import datetime

# ---------------------------------------------------------
# 1. AUTHENTICATION – Generate Access Token
# ---------------------------------------------------------

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
TOKEN_URL = "https://api.dell.com/oauth2/token"   # placeholder

# Encode client credentials
credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {"grant_type": "client_credentials"}

token_response = requests.post(TOKEN_URL, headers=headers, data=payload)
access_token = token_response.json().get("access_token")

print("Access token generated")

# ---------------------------------------------------------
# 2. API DATA RETRIEVAL
# ---------------------------------------------------------

API_URL = "https://api.dell.com/data-endpoint"   # placeholder

api_headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

response = requests.get(API_URL, headers=api_headers, timeout=60)
raw_json = response.json()

print("API data retrieved")

# ---------------------------------------------------------
# 3. TRANSFORM NESTED JSON → FLATTEN
# ---------------------------------------------------------

df = pd.json_normalize(raw_json)
df["ingestion_timestamp"] = datetime.utcnow()
df = df.convert_dtypes()

print("JSON transformed")

# ---------------------------------------------------------
# 4. SQL INSERT – Store Structured Data
# ---------------------------------------------------------

server = "your_sql_server"
database = "your_database"
table = "your_table"

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

columns = ",".join(df.columns)
placeholders = ",".join(["?"] * len(df.columns))
insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("Data inserted into SQL successfully")