# Problem 2 - Ingestion
# ---------------------
# Write code to ingest the weather data from the raw text files supplied into your database, using the model you designed. 
# Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. 
# Your code should also produce log output indicating start and end times and number of records ingested.


import os
import pandas as pd
import psycopg2
from datetime import datetime

# Database connection parameters
DB_PARAMS = {
    'dbname': 'weather_data',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432'
}

WX_DATA_DIR = "wx_data"

def ingest_file(filepath):
    # Load the file into a pandas DataFrame
    df = pd.read_csv(filepath, sep='\t', header=None, names=['date', 'max_temp', 'min_temp', 'precipitation'])

    # Replace -9999 with NaN for easier handling of missing data
    df.replace(-9999, None, inplace=True)

    # Convert date from YYYYMMDD to a proper date format
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

    # Extract station from filename
    station = os.path.splitext(os.path.basename(filepath))[0]

    # Add a new column for station
    df['station'] = station

    # Connect to the database
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()

    # Insert data into the database
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (station, date, max_temp, min_temp, precipitation)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (station, date) DO NOTHING;  -- This ensures no duplicates
        """, (row['station'], row['date'], row['max_temp'], row['min_temp'], row['precipitation']))

    conn.commit()
    cursor.close()
    conn.close()


start_time = datetime.now()
print(f"Data ingestion started at: {start_time}")
# Process each file in the wx_data directory
for filename in os.listdir(WX_DATA_DIR):
    if filename.endswith(".txt"):  # Assuming the data files have a .txt extension
        ingest_file(os.path.join(WX_DATA_DIR, filename))

end_time = datetime.now()
duration = end_time - start_time
print(f"Data ingestion ended at: {end_time}")
print(f"Duration: {duration}")


