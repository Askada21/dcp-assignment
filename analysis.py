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

# Returns the number of rows and columns
print("\nDataset shape:", df.shape)

# Display column names and data types
print("\nDataFrame information:")
df.info()

# Check missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Display descriptive statistics
print("\nDescriptive statistics:")
print(df.describe())

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Sort records chronologically
df = df.sort_values("date")

# Create a DataFrame containing only study sessions
study_df = df[df["study_status"] == "Yes"].copy()

# Create a daily DataFrame
daily_df = df.groupby("date").agg(
    study_hours=("study_hours", "sum"),
    sleep_hours=("sleep_hours", "mean"),
    productivity=("productivity", "mean")
).reset_index()

print("\nStudy sessions:")
print(study_df.head())

print("\nDaily records:")
print(daily_df.head())

# Display dataset summary
print("\nDataset Summary:")
print(f"Total records: {len(df)}")
print(f"Total unique days: {len(daily_df)}")
print(f"Total study sessions: {len(study_df)}")
print(f"Total study days: {study_df['date'].nunique()}")
print(f"Total non-study days: {(daily_df['study_hours'] == 0).sum()}")