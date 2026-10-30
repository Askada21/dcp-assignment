#Before starting work
# git pull --rebase origin main

# After updating study_tracker.csv:
# git add study_tracker.csv
# git commit -m "Add day 7"
# git push origin main

import pandas as pd

df = pd.read_csv("study_tracker.csv")

# # Define the Data Dictionary
# data_dictionary = {
#     "date": "Date of the study session (YYYY-MM-DD)",
#     "study_hours": "Number of hours spent studying (float)",
#     "subject": "Name of the subject studied (string)",
#     "productivity": "Productivity level: Low, Medium, High",
#     "study_location": "Study location: Home, Library, University, Cafe",
#     "study_status": "Session status: Planned, In Progress, Completed"
# }

#Как автоматически добавить день недели через Pandas?
#Тебе необязательно вручную записывать Monday, Tuesday и так далее.
# df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# df["day_of_week"] = df["date"].dt.day_name()

# Если хочешь, чтобы в выводе дата тоже отображалась как DD-MM-YYYY, можешь написать:
# # Convert date column to datetime
# df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Count unique days
total_days = df["date"].nunique()

print(f"Total days recorded: {total_days}")

# print(df)
print(df.to_string(index=False))
# '.to_string()' - method displays all rows and columns without shortening them with ....
# 'index=False' - removes the automatically generated row numbers (0, 1, 2, etc.) from the display.
# # Display the Data Dictionary
# for column, description in data_dictionary.items():
#     print(f"{column}: {description}")

#'df.info()' - shows the number of rows, column names, missing values, and Pandas data types.