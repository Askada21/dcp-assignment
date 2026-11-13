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

# open CSV file
with open('data/study_tracker.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)

connection.commit()
connection.close()