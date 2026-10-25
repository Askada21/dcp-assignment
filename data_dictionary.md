# Study Tracker – Data Dictionary

## Dataset Description

This dataset records my daily study sessions, including subjects studied, study hours, productivity ratings, study locations, completion status, and sleep duration.

Each row normally represents one study session. Multiple subjects can be recorded on the same date as separate entries.

Days without studying may be recorded as daily observations with zero study hours and missing session-related values.

The dataset also aims to explore potential relationships between sleep duration, study hours, and productivity.

All observations are collected and recorded manually.

## Variables

### 1. date

- **Data Type:** Date
- **Format:** DD-MM-YYYY
- **Description:** The date on which the study session or daily observation took place.
- **Example:** 16-10-2026
- **Measurement Method:** Recorded manually on the day of observation.

### 2. study_hours

- **Data Type:** Float / Numerical (Continuous)
- **Description:** Number of hours spent studying during a session.
- **Example:** 2.5
- **Unit:** Hours
- **Allowed Values:** 0 or greater
- **Measurement Method:** Study duration is recorded in minutes and converted to decimal hours.

**Examples:**

| Duration | Decimal Hours |
|---|---|
| 30 minutes | 0.50 |
| 1 hour | 1.00 |
| 1 hour 30 minutes | 1.50 |
| 2 hours 15 minutes | 2.25 |

### 3. subject

- **Data Type:** String / Categorical (Nominal)
- **Description:** Name of the subject studied during the session.
- **Examples:** Python, SQL, Analytics for Decision Making, Mathematics
- **Unit:** Not applicable
- **Measurement Method:** Recorded manually based on the subject studied.

### 4. productivity

- **Data Type:** Integer / Categorical (Ordinal)
- **Description:** Self-reported productivity rating for each study session.
- **Allowed Values:** 1–5
- **Unit:** Rating scale
- **Measurement Method:** Rated manually after each study session.

**Productivity Scale:**

| Rating | Level | Description |
|---|---|---|
| 1 | Very Low | Very little progress and frequent distractions |
| 2 | Low | Limited progress and several distractions |
| 3 | Moderate | Some useful progress and occasional distractions |
| 4 | High | Good progress and mostly focused |
| 5 | Very High | Excellent progress and highly focused |

### 5. study_location

- **Data Type:** String / Categorical (Nominal)
- **Description:** Location where the study session took place.
- **Examples:** Home, Library, University, Study Room, Cafe
- **Unit:** Not applicable
- **Measurement Method:** Recorded manually based on where studying took place.

### 6. study_status

- **Data Type:** Categorical (Binary)
- **Description:** Indicates whether the planned study session was completed.
- **Allowed Values:**
  - Yes – Completed
  - No – Not Completed
- **Unit:** Not applicable
- **Measurement Method:** Recorded based on whether the planned study session was completed.

A session marked `No` may still have recorded study hours if the planned session was not fully completed.

### 7. sleep_hours

- **Data Type:** Float / Numerical (Continuous)
- **Description:** Number of hours slept during the night before the study session. This variable is used to investigate potential relationships between sleep duration, study hours, and productivity.
- **Example:** 7.5
- **Unit:** Hours
- **Allowed Values:** 0–24
- **Measurement Method:** Sleep duration is recorded manually and converted to decimal hours.

## Data Collection Notes

- Dates are recorded in DD-MM-YYYY format.
- Study hours and sleep hours can include decimal values (e.g., 1.5 study hours or 7.5 sleep hours).
- Duration values are rounded to two decimal places.
- Productivity is measured on a scale from 1 to 5.
- Each study-session row represents one subject.
- Multiple study sessions can have the same date.
- Sleep hours refer to the previous night's sleep.
- If multiple study sessions occur on the same date, the same sleep duration is recorded for each session.
- Study status indicates whether a planned session was completed.
- Days without studying may be recorded with `study_hours = 0`, blank subject, productivity and location fields, and `study_status = No`.
- Column names and categorical values should remain consistent throughout the dataset.
- Missing observations are not invented or estimated later.
- All observations are collected and recorded manually.

## Research Questions Related to Sleep

- Is there a relationship between sleep duration and study productivity?
- Do I study more hours after getting more sleep?
- What is my average sleep duration?
- Does my productivity differ depending on how many hours I sleep?
- Is there a correlation between sleep duration and study hours?

## Additional Research Questions

- Which subjects do I spend the most time studying?
- Does study location relate to my productivity?
- How does my study duration vary across different days of the week?

## Planned Data Analysis

The dataset will be analysed using Python, Pandas, and SQLite.

The planned analysis includes:

- Calculating total and average study hours.
- Grouping study hours by subject.
- Comparing productivity ratings across study locations.
- Calculating average sleep duration.
- Investigating relationships between sleep duration and productivity.
- Comparing study duration across days of the week.

Because multiple sessions can occur on the same date, sleep duration will be counted once per date when calculating daily sleep statistics.

## Data Integrity

All observations are based on my own daily activities.

- Data is collected manually.
- No downloaded or scraped datasets are used.
- No AI-generated or synthetic data is included.
- Missing historical observations are not invented.
- GitHub commits will document the data collection process.