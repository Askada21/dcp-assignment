# DCP assignment
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

## Data Dictionary

| Column | Data Type | Description | Example |
|---|---|---|---|
| `date` | Date | Date of study session (DD-MM-YYYY) | 16-10-2026 |
| `study_hours` | Float | Number of hours spent studying | 2.5 |
| `subject` | String | Subject studied | Python |
| `productivity` | Integer (1–5) | Self-rated productivity level | 5 |
| `study_location` | Category | Location of the study session | Study Room |
| `study_status` | Binary Category | Whether the session was completed (Yes/No) | Yes |

For more information, see [Data Dictionary](data_dictionary.md).


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
