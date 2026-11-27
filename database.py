import csv 
import sqlite3
from datetime import datetime

connection = sqlite3.connect('study_tracker.db')
cursor = connection.cursor()

cursor.execute("""
create table if not exists study_tracker (
date TEXT,
study_hours REAL,
subject TEXT,
productivity INT,
study_location TEXT,
study_status TEXT,
sleep_hours REAL)
""")

# prevent duplicate imports
cursor.execute("DELETE from study_tracker")

# open csv file
with open('data/study_tracker.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file) #csv.DictReader() - reads our csv file and converts each line into a dictionary.
                                  # reads all values as strings (str), even numbers

    # insert data into SQLite
    for row in reader:

        # Missing Values
        # convert empty values to None/NULL
        for column in row:
            if row[column] == "":  # looks for a key, whose name is stored in the 'column' variable
                row[column] = None

        # Date Validation
        if row["date"] is None:
            print("Missing date")
            continue

        try:
            datetime.strptime(row["date"], "%d-%m-%Y") #strptime() - converts a string into a datetime object according to a specified format.

        except ValueError:
            print("Invalid date:", row["date"])
            continue

        # Convert Values to Correct Data Types
        # as csv.DictReader() reads CSV values as strings
        try:
            if row["study_hours"] is not None:
                row["study_hours"] = float(row["study_hours"])

            if row["productivity(1-5)"] is not None:
                row["productivity(1-5)"] = int(row["productivity(1-5)"])

            if row["sleep_hours"] is not None:
                row["sleep_hours"] = float(row["sleep_hours"])

        except ValueError:
            print("Invalid data type: ", row["date"])
            continue
        # Validate study status
        if row["study_status"] not in ["Yes", "No"]:
            print("Invalid study status:", row["date"])
            continue

        # Data Validation
        if row["study_hours"] is None or not 0 <= row["study_hours"] <= 24:
            print("Invalid study hours: ", row["study_hours"], "on", row["date"])
            continue

        if row["productivity(1-5)"] is not None and not 1 <= row["productivity(1-5)"] <= 5:
            print("Invalid productivity: ", row["productivity(1-5)"], "on", row["date"])
            continue

        if row["sleep_hours"] is not None and not 0 <= row["sleep_hours"] <= 24:
            print("Invalid sleep hours: ", row["sleep_hours"], "on", row["date"])
            continue

        # Consistency Validation
        # Check study hours when study_status is No
        if row["study_status"] == "No" and row["study_hours"] != 0:
            print("Inconsistent study hours:", row["date"])
            continue

        # Check study hours when study_status is Yes
        if row["study_status"] == "Yes" and row["study_hours"] == 0:
            print("Inconsistent study hours:", row["date"])
            continue

        # Check required values when the student studied
        if row["study_status"] == "Yes":
            if row["subject"] is None:
                print("Missing subject:", row["date"])
                continue

            if row["study_location"] is None:
                print("Missing study location:", row["date"])
                continue

            if row["productivity(1-5)"] is None:
                print("Missing productivity:", row["date"])
                continue

        # Check unnecessary values when the student did not study
        if row["study_status"] == "No":
            if row["subject"] is not None or row["study_location"] is not None or row["productivity(1-5)"] is not None:
                print("Inconsistent study record:", row["date"])
                continue
        # Insert Valid Data into SQLite
        cursor.execute(""" 
            insert into study_tracker (
                date,
                study_hours,
                subject,
                productivity,   -- Column in SQLite
                study_location,
                study_status,
                sleep_hours
            )
            values (?, ?, ?, ?, ?, ?, ?) -- -> placeholders
        """, (
            row["date"],
            row["study_hours"],
            row["subject"],
            row["productivity(1-5)"],    # Column in CSV
            row["study_location"],
            row["study_status"],
            row["sleep_hours"]
        )
    )

connection.commit()

# check inserted records
cursor.execute("select * from study_tracker")

rows = cursor.fetchall()

for row in rows:
    print(row)

# count the records
cursor.execute("select count(*) from study_tracker")

total_rows = cursor.fetchone()[0]
print("Total records: ", total_rows)

connection.close()

print("Data inserted successfully!")