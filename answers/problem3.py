# Problem 3 - Data Analysis
# -------------------------
# For every year, for every weather station, calculate:
# * Average maximum temperature (in degrees Celsius)
# * Average minimum temperature (in degrees Celsius)
# * Total accumulated precipitation (in centimeters)

# Ignore missing data when calculating these statistics.
# Design a new data model to store the results. Use NULL for statistics that cannot be calculated.
# Your answer should include the new model definition as well as the code used to calculate the new values and store them in the database.


import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(
    dbname="weather_data",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

# Get distinct station IDs and years
cursor.execute("""
    SELECT DISTINCT station, EXTRACT(YEAR FROM date)
    FROM weather_data
""")
stations_and_years = cursor.fetchall()

cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_stats (
    id SERIAL PRIMARY KEY,
    station VARCHAR(255),
    year INT,
    avg_max_temp FLOAT,
    avg_min_temp FLOAT,
    total_precipitation FLOAT
)
''')

for station, year in stations_and_years:
    # Calculate statistics
    cursor.execute(sql.SQL("""
        INSERT INTO weather_stats (station, year, avg_max_temp, avg_min_temp, total_precipitation)
        SELECT 
            %s,
            %s,
            AVG(max_temp) FILTER (WHERE max_temp > -9999),
            AVG(min_temp) FILTER (WHERE min_temp > -9999),
            SUM(precipitation) FILTER (WHERE precipitation > -9999) / 10
        FROM 
            weather_data 
        WHERE 
            station = %s AND EXTRACT(YEAR FROM date) = %s
    """), (station, year, station, year))

connection.commit()
cursor.close()
connection.close()
