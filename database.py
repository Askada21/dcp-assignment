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
cursor.execute("delete from study_tracker")

# open csv file
with open('data/study_tracker.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file) #csv.DictReader() - reads our csv file and converts each line into a dictionary.
                                  # reads all values as strings (str), even numbers

    # insert data into SQLite
    for row in reader:
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
            values (?, ?, ?, ?, ?, ?, ?)
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
connection.close()

print("Data inserted successfully!")