# Problem 2 - Ingestion
# ---------------------
# Write code to ingest the weather data from the raw text files supplied into your database, using the model you designed. 
# Check for duplicates: if your code is run twice, you should not end up with multiple rows with the same data in your database. 
#Your code should also produce log output indicating start and end times and number of records ingested.

# Import required modules and libraries
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

WX_DATA_DIR = "./wx_data"  # Directory containing raw weather data files

def ingest_file(filepath):
    # Load the raw weather data file into a pandas DataFrame
    df = pd.read_csv(filepath, sep='\t', header=None, names=['date', 'max_temp', 'min_temp', 'precipitation'])

    # Replace missing data represented by -9999 with None (null values)
    df.replace(-9999, None, inplace=True)

    # Convert date from YYYYMMDD format to a proper datetime object
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

    # Extract the station identifier from the filename
    station = os.path.splitext(os.path.basename(filepath))[0]

    # Add a new column for station to the DataFrame
    df['station'] = station

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()

    # Insert data into the weather_data table, avoid duplicates by using ON CONFLICT
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (station, date, max_temp, min_temp, precipitation)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (station, date) DO NOTHING;  -- Skip insertion if the same station and date exist
        """, (row['station'], row['date'], row['max_temp'], row['min_temp'], row['precipitation']))
        
        # Print progress every 1000 rows to avoid flooding the console
        if index % 1000 == 0:
            print(f"{index + 1} records processed from file: {filepath}")

    # Commit the changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    # Print completion message for this file
    print(f"File {filepath} has been ingested successfully.")

# Log the start time of the ingestion process
start_time = datetime.now()
print(f"Data ingestion started at: {start_time}")

# Process each weather data file in the wx_data directory
for filename in os.listdir(WX_DATA_DIR):
    if filename.endswith(".txt"):  # Only process .txt files
        print(f"Processing file: {filename}")
        ingest_file(os.path.join(WX_DATA_DIR, filename))

# Log the end time of the ingestion process and calculate duration
end_time = datetime.now()
duration = end_time - start_time
print(f"Data ingestion ended at: {end_time}")
print(f"Total Duration: {duration}")
