# Study Tracker – Data Dictionary

## Dataset Description

This dataset records my daily study sessions, including subjects studied, study hours, productivity ratings, study locations, and completion status.

Each row represents one study session. Multiple subjects can be recorded on the same date as separate entries.

## Variables

### 1. date
- **Data Type:** Date
- **Format:** DD-MM-YYYY
- **Description:** The date on which the study session took place.
- **Example:** 16-10-2026

### 2. study_hours
- **Data Type:** Float
- **Description:** Number of hours spent studying during a session.
- **Example:** 2.5
- **Unit:** Hours

### 3. subject
- **Data Type:** String / Categorical (Nominal)
- **Description:** Name of the subject studied during the session.
- **Examples:** Python, SQL, Analytics for Decision Making, Mathematics

### 4. productivity
- **Data Type:** Integer / Categorical (Ordinal)
- **Description:** Self-reported productivity rating for each study session.
- **Allowed Values:**
  - 1 – Very Low
  - 2 – Low
  - 3 – Moderate
  - 4 – High
  - 5 – Very High

### 5. study_location
- **Data Type:** String / Categorical (Nominal)
- **Description:** Location where the study session took place.
- **Examples:** Home, Library, University, Study Room, Cafe

### 6. study_status
- **Data Type:** Categorical (Binary)
- **Description:** Indicates whether the study session was completed.
- **Allowed Values:**
  - Yes – Completed
  - No – Not Completed

## Data Collection Notes

- Dates are recorded in DD-MM-YYYY format.
- Study hours can include decimal values (e.g., 1.5 hours).
- Productivity is measured on a scale from 1 to 5.
- Each row represents one study session for one subject.
- Multiple study sessions can have the same date.
- Column names and categorical values should remain consistent throughout the dataset.