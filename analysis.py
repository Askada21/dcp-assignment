import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
connection = sqlite3.connect("study_tracker.db")

# Load the study tracker table into a pandas DataFrame
df = pd.read_sql("select * from study_tracker", connection)

connection.close()

# Display the first five records
print(df.head())