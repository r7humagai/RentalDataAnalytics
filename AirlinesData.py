"""
Objective: Data Analysis Project using SQL for identification of opportunities to increase occupancy
           on low-performing flights.
Goals:     Increased Profitability for the airlines.
"""

# Importing Libraries

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Database Connections

connection = sqlite3.connect('travel.sqlite')
cursor = connection.cursor()        # Used for executing queries

cursor.execute("""select name from sqlite_master where type = 'table';""")
print('List of tables present in the database')
table_list = [table[0] for table in cursor.fetchall()]
print(table_list)

# Data Exploration
# Aircraft_Data
aircrafts_data = pd.read_sql_query("select * from aircrafts_data", connection)
print(type(aircrafts_data))
print(aircrafts_data.head(4))

# Print number of rows and columns
print(aircrafts_data.shape)

# Airports_Data
airports_data = pd.read_sql_query("select * from airports_data", connection)
print(airports_data.head())
print(airports_data.shape)

#Boarding Passes
boarding_passes = pd.read_sql_query("select * from boarding_passes", connection)
print(boarding_passes.head())
print(boarding_passes.shape)