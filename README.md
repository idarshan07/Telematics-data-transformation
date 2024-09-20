# Telematics-data-transformation
### This repository provides python script to load, clean and transform telematics data.

## Repository structure
- **"input"** : input folder containes input json data file
- **"output"** : output folder contains output parquet data file
- **requirements.txt** : Required python modules
- **data_transformation.py** : includes required function to load, transform and save transformed data
- **test_conversion.py** : includes unit tests for convert_duration function to demonstrate correctness of conversion of duration fields into seconds

## Assumptions
- All calculations of durations are correct.
- "nextTripStart", start" and "stop" datetime values are in "ISO8601" format
- duration fields are in d.HH:MM:SS format
- "engineHours" is also a duration field but have not been converted in seconds due to missing values.
- note: Scripts written in Python 3.12.5

## Quick start
- clone this repository.
- run data_transformation.py
    - load_data function will read json file and load data into pandas dataframe.
    - convert_duration function can convert duration fields in seconds from d.HH:MM:SS format
    - data_transform function can apply data_transformation on duration fields, convert 3 columns in datetime format and remove duplicate rows from dataframe(there is no duplicate value in given data).
    - Also it drops 11 rows where averageSpeed is null because data shows those vehicle did not make any trips and drops "engineHours" column as it has 2101 missing observations.
    - save_output function writes cleaned data in parquet file in output folder.
- run test_conversion.py
    - pyhton -m unittest -v test_conversion.py
    - It runs unit tests on convert_duration function which converts duration fields in seconds.
    - follow comments in code and make changes in 'duration' and 'expected_durations' to further verify different datetime values.
