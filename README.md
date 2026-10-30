# Data Centric Programming Assignment 2026

**Project:** Personal Study Tracker

- [Assignment Brief](dataset_assignment.md)

This project is part of the Data Centric Programming module and focuses on tracking and analysing my personal study habits. It involves manually collecting data about my study sessions, including study hours, subjects, productivity ratings, study locations, study status, and sleep duration. The collected data will be stored and validated using Python and SQLite, analysed using Pandas, and visualised using Matplotlib. An interactive application will also be developed to explore the results.

All data is collected through my own daily observations. No downloaded, scraped, AI-generated, or retrospectively estimated data will be used.

# Questions

The main goal of this project is to investigate my personal study habits using data collected manually throughout the semester.

The research questions are:

**1. Is there a relationship between sleep duration and study productivity?**

**2. Which subjects do I spend the most time studying?**

**3. Does study location relate to my productivity?**

Additional questions:

- What is my average sleep duration?
- Do I study more hours after getting more sleep?
- How does my study duration vary across different days of the week?

# Data Dictionary

The dataset contains information about my daily study sessions, including study hours, subjects, productivity ratings, study locations, completion status, and sleep duration.

| Column | Data Type | Unit / Values | Description | Example |
|---|---|---|---|---|
| `date` | Date | DD-MM-YYYY | Date of the study session or daily observation | 16-10-2026 |
| `study_hours` | Float | Hours | Number of hours spent studying | 2.50 |
| `subject` | String / Categorical (Nominal) | Subject name | Subject studied during the session | Data Centric Programming |
| `productivity` | Integer / Categorical (Ordinal) | 1–5 | Self-rated productivity level | 5 |
| `study_location` | Categorical (Nominal) | Home, Library, University, Study Room, Cafe | Location of the study session | Study Room |
| `study_status` | Categorical (Binary) | Yes / No | Whether I studied on that day | Yes |
| `sleep_hours` | Float / Numerical (Continuous) | Hours | Number of hours slept during the previous night | 7.50 |

### Data Collection Rules

- All data is collected and recorded manually.
- Dates are recorded in DD-MM-YYYY format.
- Study hours and sleep hours are recorded in decimal hours and rounded to a maximum of two decimal places. Whole numbers are recorded without decimal places.
- Productivity is self-rated on a scale from 1 (Very Low) to 5 (Very High).
- Each study-session row represents one subject.
- Multiple study sessions may occur on the same date.
- Sleep duration refers to the previous night's sleep.
- When multiple sessions occur on the same date, the same sleep duration is recorded for each session.
- Study status indicates whether I studied on a particular day (Yes = Studied, No = Did not study).
- Days without studying may be recorded with zero study hours and empty session-related fields.
- Missing observations are not invented or estimated later.

For more detailed information about each variable and its measurement method, see the [Data Dictionary](data_dictionary.md).

# Description of the project

The Personal Study Tracker is a Data Centric Programming project that focuses on collecting and analysing my daily study habits.

The purpose of this project is to understand how much time I spend studying, which subjects require the most attention, and whether factors such as sleep duration and study location are related to my productivity.

I am collecting my own data by recording study sessions, study hours, subjects, productivity ratings, study locations, study status, and sleep duration.

The data is stored in a CSV file and will be used to develop a Python application.

The final application is planned to use:

- **Python** for programming and data processing.
- **CSV** for storing the original manually collected dataset.
- **SQLite** for database storage.
- **Pandas** for data analysis.
- **Matplotlib** for data visualisation.
- **Git and GitHub** for version control and documentation.

<!--The application will allow users to explore the collected data, perform calculations, compare study habits, and display visualisations. -->

The project is currently in the data collection and planning stage.

# Instructions for use

The project is currently under development.

The collected data is stored in `study_tracker.csv`.

**Requirements:**
- Python 3
- Pandas
- VS Code or another Python development environment

**To view the initial dataset:**

1. Clone or download the GitHub repository.
2. Open the project folder in VS Code or another Python development environment.
3. Make sure Python 3 is installed.
4. Install Pandas if it is not already installed:

   ```bash
   python3 -m pip install pandas
   ```

5. Run `main.py` using Python 3:

   ```bash
   python3 main.py
   ```

The full application instructions will be added as the project develops.

# How it works:

Currently, study observations are recorded manually in `study_tracker.csv`.

Each record contains information about the date, study duration, subject, productivity, location, study status, and sleep duration.

The planned application workflow is:

1. Read the collected CSV data using Python.
2. Validate the data and handle missing values.
3. Store the validated records in an SQLite database.
4. Retrieve data from the database using SQL queries.
5. Analyse the data using Pandas.
6. Create visualisations using Matplotlib.
7. Allow users to explore the dataset through an interactive menu.

The application is still being developed, so these steps describe the planned final functionality.

# Findings

The project is currently in the data collection stage.

Findings will be added after enough observations have been collected and analysed.

The analysis will focus on the research questions, including the relationship between sleep and productivity, time spent studying different subjects, and productivity across study locations.

<!-- # List of files in the project

| Files | Source |
|---|---|
| `README.md` | Project documentation and proposal, prepared with AI writing assistance |
| `data_dictionary.md` | Data dictionary based on my own collection rules, prepared with AI writing assistance |
| `study_tracker.csv` | Self-collected and manually recorded data |
| `main.py` | Initial Python script; source and any external assistance to be documented |
| `dataset_assignment.md` | Assignment brief provided by the lecturer, if included in the repository | -->

# References

- Data Centric Programming Assignment 2026 – assignment brief and README template provided by the lecturer.
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
<!--- [SQLite Documentation](https://www.sqlite.org/docs.html) -->

<!-- # What I am most proud of in the assignment

At this stage, I am focusing on developing an original dataset based on my own daily study activities.

The project allows me to investigate questions that are personally relevant to my study habits.

This section will be updated as the application develops and the analysis is completed. -->

<!-- # What I learned

So far, this project has involved planning a dataset, defining different data types, organising information in CSV format, and documenting how observations are collected.

I am also developing my understanding of how Pandas can be used to work with structured data.

This section will be expanded as I implement database storage, data analysis, visualisations, and interactive features. -->


<!-- ========== STUDY TRACKER ==========

1. View all study sessions
2. Search by subject
3. Calculate total study hours
4. Calculate average productivity
5. Analyse sleep and productivity
6. Display charts
7. Add a study session
0. Exit

Select an option: 


for question's diagrams:
1. Scatter plot - sleep_hours against productivity
2. Bar chart - total_hours per subjects 
3. Bar chart - average of productivity by study location-->