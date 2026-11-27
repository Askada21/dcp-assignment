import sqlite3

# SQL queries and data retrieval

connection = sqlite3.connect("study_tracker.db")
cursor = connection.cursor()

# Calculate total study hours for each subject
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

# Calculate average productivity for each study location
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

# Count the number of study sessions for each subject
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

connection.close()