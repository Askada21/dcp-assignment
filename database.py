import csv 
import sqlite3

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

        # Convert Values to Correct Data Types
        # as csv.DictReader() reads CSV values as strings
        if row["study_hours"] is not None:
            row["study_hours"] = float(row["study_hours"])

        if row["productivity(1-5)"] is not None:
            row["productivity(1-5)"] = int(row["productivity(1-5)"])

        if row["sleep_hours"] is not None:
            row["sleep_hours"] = float(row["sleep_hours"])

        # Data Validation
        

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