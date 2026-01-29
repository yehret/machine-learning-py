import requests
import json
import os
import time

# Configuration
API_KEY = "z2Ax9lOoeM1J58k4xqb1Snf83RWpmBvfUXroucJL" 
URL = "https://api.nasa.gov/planetary/apod"
SAVE_PATH = "../data/raw/space_data.json"

def fetch_year(year):
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    params = {
        "api_key": API_KEY,
        "start_date": start_date,
        "end_date": end_date
    }
    
    print(f"--- Fetching {year} ---")
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        new_data = response.json()
        print(f"Success! Received {len(new_data)} entries for {year}.")
        return new_data
    else:
        print(f"Failed {year}. Error: {response.status_code} - {response.text}")
        return []

def main():
    years_to_fetch = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    
    master_data = []
    
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, 'r') as f:
            try:
                master_data = json.load(f)
                print(f"Loaded {len(master_data)} existing entries from file.")
            except json.JSONDecodeError:
                print("Existing file was empty or corrupted. Starting fresh.")

    for year in years_to_fetch:
        year_data = fetch_year(year)
        if year_data:
            master_data.extend(year_data)
            
            os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
            with open(SAVE_PATH, 'w') as f:
                json.dump(master_data, f, indent=4)
            print(f"Master file updated. Total entries: {len(master_data)}")
            
            time.sleep(60) 

if __name__ == "__main__":
    main()