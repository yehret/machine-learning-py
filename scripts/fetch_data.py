import requests
import json
import os

API_KEY = "z2Ax9lOoeM1J58k4xqb1Snf83RWpmBvfUXroucJL" 
URL = "https://api.nasa.gov/planetary/apod"
SAVE_PATH = "../data/raw/space_data.json"

def manual_fetch(start_date, end_date):
    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }
    
    print(f"Fetching data from {start_date} to {end_date}...")
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        
        with open(SAVE_PATH, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Success! Saved {len(data)} entries to {SAVE_PATH}")
    else:
        print(f"Failed. Error Code: {response.status_code}: {response.text}")

if __name__ == "__main__":
    manual_fetch("2015-01-01", "2026-01-20")