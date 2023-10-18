import pandas as pd
import numpy as np
import json

# Set the display options to show all columns
pd.set_option('display.max_columns', None)

# Prevent truncation of cell contents
pd.set_option('display.max_colwidth', None)

# read activities file
activities_filepath = 'data_original/strava_activities.csv'
strava_activities_df = pd.read_csv(activities_filepath)
print("------------------------------------- strava_activities_df - head -------------------------------------")
print(strava_activities_df.head())
print("-------------------------------------------------------------------------------------------------------")

# read zones file
strava_zones_filepath = 'data_original/strava_zones_per_activity.csv'
strava_zones_df = pd.read_csv(strava_zones_filepath)
print("------------------------------------- strava_zones_df - head ------------------------------------------")
print(strava_zones_df.head())
print("-------------------------------------------------------------------------------------------------------")

# check if zones have Nan values
zones_having_nulls = strava_zones_df[strava_zones_df.isna().any(axis=1)]
print("------------------------------------- zones_having_nulls - head ---------------------------------------")
print(zones_having_nulls.head(5))
print("-------------------------------------------------------------------------------------------------------")

# create new df same as activities, create columns for 5 HR zones and 11 power zones
activities_with_zones = strava_activities_df.copy()

for i in range(1, 6):
    activities_with_zones[f'HR Zone {i}'] = np.nan

for i in range(1, 12):
    activities_with_zones[f'Power Zone {i}'] = np.nan

print("------------------------------------- activities_with_zones - head ------------------------------------")
print(activities_with_zones.head())
print("-------------------------------------------------------------------------------------------------------")

# Get the zones from zones file and set the matched columns in new activities df as per their resp zones
col_dropped_zones = strava_zones_df.drop(columns='Unnamed: 0')

for idx, row in col_dropped_zones.iterrows():
    id = None
    hr_zones = []
    power_zones = []
    
    for col in row.iloc[:]:
        if not pd.isnull(col):
            repl_col = col.replace("'", '"').replace('True', 'true').replace('False', 'false').replace('None', 'null')
            conv_col = json.loads(repl_col)

            if 'id' in conv_col:
                id = conv_col['id']

            if 'type' in conv_col:
                col_type = conv_col['type']
                
                if col_type == 'heartrate' and 'distribution_buckets' in conv_col and conv_col['distribution_buckets'] != None and len(conv_col['distribution_buckets']) == 5:
                    buckets = conv_col['distribution_buckets']
                    for bucket in buckets:
                        hr_zones.append(bucket['time'])
                elif col_type == 'power' and 'distribution_buckets' in conv_col and conv_col['distribution_buckets'] != None and len(conv_col['distribution_buckets']) == 11:
                    buckets = conv_col['distribution_buckets']
                    for bucket in buckets:
                        power_zones.append(bucket['time'])

    if id != None:
        if len(hr_zones) == 5:
            for i in range(1, 6):
                activities_with_zones.loc[activities_with_zones['id'] == id, f'HR Zone {i}'] = hr_zones[i-1]    
        if len(power_zones) == 11:
            for i in range(1, 12):
                activities_with_zones.loc[activities_with_zones['id'] == id, f'Power Zone {i}'] = power_zones[i-1]

print("------------------------------------- activities_with_zones - head ------------------------------------")
print(activities_with_zones.head())
print("-------------------------------------------------------------------------------------------------------")

# saving current state - activities with zones - to csv as checkpoint
activities_with_zones.to_csv('data_processed/activities_with_zones.csv')