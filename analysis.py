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

# Question 1: Which subject do I spend the most time studying?
def study_hours_by_subject(data):
    # Calculate total study hours for each subject
    subject_hours = data.groupby("subject")["study_hours"].sum()

    # Sort subjects from highest to lowest study hours
    subject_hours = subject_hours.sort_values(ascending=False)

    print("\nTotal study hours by subject:")
    print(subject_hours.round(2))

    return subject_hours

# Create a bar chart showing total study hours by subject
def plot_study_hours_by_subject(subject_hours):
    plt.figure(figsize=(10, 6))

    subject_hours.plot(kind="bar", color="steelblue")

    plt.title("Total Study Hours by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Total Study Hours")

    plt.xticks(rotation=45, ha="right") #Rotates subject names to prevent overlapping
    plt.tight_layout() #Prevents labels from being cut off

    plt.savefig("charts/study_hours_by_subject.png", dpi=300)

    plt.show()
subject_hours = study_hours_by_subject(study_df)
plot_study_hours_by_subject(subject_hours)

# Question 2: Where am I most productive when studying?
def productivity_by_location(data):
    # Calculate average productivity for each location
    location_productivity = data.groupby("study_location")["productivity"].mean()

    # Sort locations from highest to lowest productivity
    location_productivity = location_productivity.sort_values(ascending=False)

    print("\nAverage productivity by study location:")
    print(location_productivity.round(2))

    # Count study sessions for each location
    print("\nNumber of study sessions by location:")
    print(data["study_location"].value_counts())

    return location_productivity

# Create a bar chart showing average productivity by location
def plot_productivity_by_location(location_productivity):
    plt.figure(figsize=(8, 5))

    location_productivity.plot(kind="bar", color="seagreen")

    plt.title("Average Productivity by Study Location")
    plt.xlabel("Study Location")
    plt.ylabel("Average Productivity")

    # Set the productivity scale from 0 to 5
    plt.ylim(0, 5)

    plt.xticks(rotation=0)
    plt.tight_layout()

    # Save the chart
    plt.savefig("charts/productivity_by_location.png", dpi=300)

    plt.show()
location_productivity = productivity_by_location(study_df)
plot_productivity_by_location(location_productivity)