# DCP assignment
# DCP Assignment – Personal Study Tracker

## Project Proposal

### Project Overview

The Personal Study Tracker is a Data Centric Programming project that focuses on collecting and analysing my daily study habits.

The aim of this project is to understand how much time I spend studying, which subjects I study most frequently, and whether factors such as sleep duration and study location are related to my productivity.

I am collecting my own data manually by recording study sessions, subjects, productivity ratings, study locations, session completion status, and sleep duration.

The collected data will be used to develop a Python application that stores information in a database, analyses it using Pandas, and presents results through visualisations and an interactive interface.

## Project Objectives

- Collect original data about my daily study habits.
- Record the duration of study sessions and the subjects studied.
- Track productivity levels and study locations.
- Record sleep duration to investigate potential relationships with productivity.
- Analyse patterns in study habits using Python and Pandas.
- Store the collected data in an SQLite database.
- Create visualisations using Matplotlib.
- Develop an interactive application for exploring the dataset.

## Research Questions

The main research questions are:

1. Is there a relationship between sleep duration and study productivity?
2. Which subjects do I spend the most time studying?
3. Does study location relate to my productivity?

### Additional Questions

- What is my average sleep duration?
- Do I study more hours after getting more sleep?
- How does my study duration vary across different days of the week?

## Dataset Description

The dataset records my daily study sessions, including subjects studied, study hours, productivity ratings, study locations, completion status, and sleep duration.

Each row normally represents one study session for one subject. Multiple subjects can be recorded on the same date as separate entries.

Days without studying may also be recorded with zero study hours and empty session-related fields.

The dataset is stored in `study_tracker.csv`.

All observations are collected and recorded manually.

## Data Dictionary

| Column | Data Type | Unit / Values | Description | Example |
|---|---|---|---|---|
| `date` | Date | DD-MM-YYYY | Date of the study session or daily observation | 16-10-2026 |
| `study_hours` | Float | Hours | Number of hours spent studying | 2.5 |
| `subject` | String / Categorical | Subject studied | Name of the subject | Python |
| `productivity` | Integer / Ordinal | 1–5 | Self-rated productivity level | 5 |
| `study_location` | Categorical | Home, Library, University, Study Room, Cafe | Location of the study session | Study Room |
| `study_status` | Binary Categorical | Yes / No | Whether the planned study session was completed | Yes |
| `sleep_hours` | Float | Hours | Number of hours slept the previous night | 7.5 |

For detailed variable definitions, measurement methods, and data collection rules, see the [Data Dictionary](data_dictionary.md).

## Data Collection Method

The dataset is created from my own daily observations.

- Dates are recorded in DD-MM-YYYY format.
- Study duration is recorded in decimal hours.
- Productivity is self-rated on a scale from 1 to 5.
- Study location is recorded for each session.
- Study status indicates whether the planned session was completed.
- Sleep duration refers to the previous night's sleep.
- Multiple study sessions can be recorded on the same date.
- All values are recorded manually rather than generated or downloaded.

## Technologies

The project will use:

- **Python** – Programming and data processing.
- **CSV** – Initial data storage.
- **SQLite** – Database storage.
- **Pandas** – Data analysis.
- **Matplotlib** – Data visualisation.
- **Git and GitHub** – Version control and project documentation.

## Planned Application Features

The final application is planned to include:

1. Viewing recorded study sessions.
2. Searching and filtering study data.
3. Calculating total and average study hours.
4. Comparing study time across subjects.
5. Analysing productivity and sleep duration.
6. Displaying charts and visualisations.
7. An interactive menu for exploring the dataset.
8. The ability to add new study sessions.

## Current Progress

The project is currently in the data collection and planning stage.

- The GitHub repository has been created.
- The dataset structure has been defined.
- Initial study observations have been recorded in a CSV file.
- The data dictionary has been prepared.
- Research questions have been identified.
- Initial Python work has focused on reading the CSV dataset.

The next steps are to continue collecting data, implement SQLite database storage, and develop the analysis and interactive application.

## Data Collection and Academic Integrity

All dataset observations are collected manually from my own study activities.

The dataset does not use downloaded, scraped, synthetic, or AI-generated observations.
<!-- ## Student Study Habits & Productivity Tracker
(StudyTrack - Personal Study Habits Analysis Using Python & Pandas) <br>
- The purpose of this assignment: How do my study habits, study time, breaks, and daily activities affect my productivity? <br>
# Study Tracker – Data Centric Programming Assignment

## Project Overview

Study Tracker is a Python-based project developed as part of my Data Centric Programming module at Technological University Dublin (TU Dublin).

The aim of this project is to collect, manage, and analyse my personal study habits using **Python and Pandas**.

The dataset contains manually collected information about my daily study sessions, including:

- **Date** – When the study session took place.
- **Subject** – The subject studied (Python, SQL, Analytics, etc.).
- **Study Hours** – Time spent studying, recorded in decimal hours.
- **Productivity** – Self-rated productivity on a scale from 1 to 5.
- **Study Location** – Where I studied (Home, Library, University, etc.).
- **Study Status** – Whether the study session was completed (Yes/No).
- **Sleep Hours** – Hours slept the previous night.

Each row represents one study session, and multiple subjects can be recorded on the same date.

## Project Objectives

The main objectives are to:

1. Create and maintain an original CSV dataset containing at least 50 observations.
2. Use Pandas to load, clean, and explore the collected data.
3. Analyse study habits, productivity, and sleep patterns.
4. Identify relationships between study duration, sleep, and productivity.
5. Visualise findings using charts and graphs.

## Research Questions

- How many hours do I study on average per day?
- Which subjects do I spend the most time studying?
- On which days of the week do I study the most?
- Which study location is associated with the highest productivity?
- Is there a correlation between sleep duration and productivity?
- How many days do I study compared to days off?

## Technologies

- **Python** – Programming and data analysis
- **Pandas** – Data manipulation and statistical analysis
- **CSV** – Storage of manually collected observations
- **Matplotlib** – Data visualisation

## Current Progress

The initial dataset structure and data dictionary have been defined. Daily observations are being collected in a CSV file, which is read using Pandas.

Further analysis and visualisations will be developed as more data becomes available.

===== STUDY TRACKER =====

1. Add study session
2. View all records
3. View total study hours
4. Compare subjects
5. Analyse productivity
6. Generate charts
7. Exit

Choose an option:
<br>
# OR
========== STUDY TRACKER ==========

1. Add a study session
2. View all study sessions
3. Update or delete a session
4. View total study hours
5. Compare study subjects
6. Analyse productivity
7. Generate charts
8. Exit

Select an option:
<br>
## Project Structure

```text
dcp-assignment/
├── main.py              # Python script for data analysis
├── study_tracker.csv    # Dataset containing study sessions
├── data_dictionary.md   # Dataset documentation
└── README.md            # Project overview
```

## Dataset

The dataset contains records of my study sessions, including time spent studying, subjects, productivity ratings, study locations, and completion status.

Each row represents one study session. Multiple sessions can be recorded on the same date. -->

<!-- ## Research Questions & Pandas Analysis

The goal of this project is to analyse my personal study habits, track the time spent studying different subjects, and explore patterns in my productivity using Python and Pandas.

The following research questions will guide the analysis:

| Research Question | Pandas Technique |
|---|---|
| How many hours do I study on average per day? | `groupby()` + `sum()` + `mean()` |
| Which subject do I spend the most time studying? | `groupby()` + `sum()` |
| On which day of the week do I study the most? | `groupby()` + `sum()` |
| Do I study more at home, in the library, or at university? | `groupby()` + `sum()` |
| Which study location has the highest average productivity? | `groupby()` + `mean()` |
| Is there a relationship between study hours and productivity? | `corr()` |
| How many days did I study versus take a day off? | `groupby()` + `count()` |
| How does my study time change throughout the semester? | `groupby()` + Data Visualisation |


### Sleep & Productivity Analysis

The dataset also includes sleep duration to investigate potential relationships between sleeping habits and academic productivity.

| Research Question | Pandas Technique |
|---|---|
| How many hours do I sleep on average? | `groupby()` + `mean()` |
| Is there a correlation between sleep duration and productivity? | `corr()` |
| Do I study longer after getting more sleep? | `corr()` |
| What is my average productivity after sleeping less than 7 hours? | Filtering + `mean()` |
| How does productivity vary across different sleep durations? | `groupby()` + `mean()` |

The aim is to identify possible relationships between sleep duration, study time, and self-reported productivity.
### Expected Outcomes

By analysing my dataset, I aim to:

- Identify which subjects require the most study time.
- Understand my average daily study hours.
- Compare productivity across different study locations.
- Explore the relationship between study duration and productivity.
- Identify patterns in my study routine throughout the semester.
- Visualise study habits using charts and graphs.

### Technologies

- **Python** — Data processing and analysis
- **Pandas** — Data manipulation and statistical analysis
- **CSV** — Storage of manually collected data
- **Matplotlib** — Data visualisation -->
