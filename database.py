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