import requests
import json
import os

API_KEY = "z2Ax9lOoeM1J58k4xqb1Snf83RWpmBvfUXroucJL" 
SAVE_PATH = "../data/raw/apod_data.json"

def fetch_apod_batch(start_date, end_date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&start_date={start_date}&end_date={end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

data = fetch_apod_batch("2020-01-01", "2025-12-31")

os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

with open(SAVE_PATH, 'w') as f:
    json.dump(data, f)
    print(f"Saved {len(data)} descriptions to {SAVE_PATH}")