import sqlite3

# SQL queries and data retrieval

connection = sqlite3.connect("study_tracker.db")
cursor = connection.cursor()

# Dataset Overview
cursor.execute("""
    select count(*) as total_records,
    count(distinct date) as total_days
    from study_tracker
""")

row = cursor.fetchone()

print("Dataset Overview:")
print(f"Total records: {row[0]}")
print(f"Total days recorded: {row[1]}\n")

# Count total study sessions
cursor.execute("""
    select count(*)
    from study_tracker
    where study_status = 'Yes'
""")

total_sessions = cursor.fetchone()[0]

print(f"Total study sessions: {total_sessions}\n")

# 1. Calculate total study hours for each subject
# Exclude non-study days and sort from highest to lowest
cursor.execute("""
    select subject, sum(study_hours) as total_hours
    from study_tracker
    where study_status = 'Yes'
    group by subject
    order by total_hours desc
""")

rows = cursor.fetchall()

print("Total study hours by subject: ")

# Convert decimal hours into hours and minutes for display
for row in rows:
    subject = row[0]
    total_hours = row[1]

    total_minutes = round(total_hours * 60)
    hours = total_minutes // 60 # Get whole hours
    minutes = total_minutes % 60 # Get remaining minutes

    print(f"{subject}: {hours}h {minutes}m")

# 2. Calculate average productivity for each study location
cursor.execute("""
    select study_location, round(avg(productivity), 2) as avg_productivity
    from study_tracker
    where study_status = 'Yes'
    group by study_location
    order by avg_productivity desc
""")

rows = cursor.fetchall()

print("\nAverage productivity by study location:")

for row in rows:
    location = row[0]
    avg_productivity = row[1]

    print(f"{location}: {avg_productivity}-5")

# 3. Count the number of study sessions for each subject
cursor.execute("""
    select subject, count(*) as total_sessions
    from study_tracker
    where study_status = 'Yes'
    group by subject
    order by total_sessions desc
""")

rows = cursor.fetchall()

print("\nNumber of study sessions per subject:")

for row in rows:
    subject = row[0]
    total_sessions = row[1]

    print(f"{subject}: {total_sessions} sessions")

# 4. Find study sessions longer than two hours
cursor.execute("""
    select date, subject, study_hours, productivity
    from study_tracker
    where study_hours > 2 and study_status = 'Yes'
    order by study_hours desc
""")

rows = cursor.fetchall()

print("\nStudy sessions longer than two hours:")

for row in rows:
    date = row[0]
    subject = row[1]
    study_hours = row[2]
    productivity = row[3]

    # Convert decimal hours into hours and minutes
    total_minutes = round(study_hours * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"{date} | {subject} | {hours}h {minutes}m | Productivity: {productivity}/5")

# 5. Calculate average sleep hours without counting the same day multiple times
cursor.execute("""
    select round(avg(sleep_hours), 2) as avg_sleep
    from (
        select date, avg(sleep_hours) as sleep_hours
        from study_tracker
        where sleep_hours is not null
        group by date
    )
""")

avg_sleep = cursor.fetchone()[0]

# Convert decimal hours into hours and minutes
total_minutes = round(avg_sleep * 60)
hours = total_minutes // 60
minutes = total_minutes % 60

print(f"\nAverage sleep per night: {hours}h {minutes}m")

# 6. Count unique study and non-study days
cursor.execute("""
    select study_status, count(distinct date) as total_days
    from study_tracker
    group by study_status
    order by total_days desc
""")

rows = cursor.fetchall()

print("\nNumber of study and non-study days:")

for row in rows:
    status = row[0]
    total_days = row[1]

    if status == "Yes":
        print(f"Study days: {total_days}")
    else:
        print(f"Non-study days: {total_days}")

connection.close()