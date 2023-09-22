
# Problem 1 - Data Modeling
# -------------------------
# Choose a database to use for this coding exercise (SQLite, Postgres, etc.). 
# Design a data model to represent the weather data records. If you use an ORM, your answer should be in the form of that ORM's data definition format. 
# If you use pure SQL, your answer should be in the form of DDL statements.

import psycopg2

# Set up the PostgreSQL database connection
connection = psycopg2.connect(
    dbname="weather_data", # database name
    user="postgres", 
    password="1234",
    host="localhost",  #  database host
    port="5432"  # database port
)

cursor = connection.cursor()

# Create a table structure for weather data
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    station VARCHAR(255),
    date DATE,  -- This will store date in the format "YYYY-MM-DD"
    max_temp INTEGER,
    min_temp INTEGER,
    precipitation INTEGER,
    UNIQUE (station, date)
)
''')
               
connection.commit()

cursor.close()
connection.close()