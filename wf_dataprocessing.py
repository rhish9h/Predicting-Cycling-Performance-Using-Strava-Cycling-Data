import pandas as pd
import numpy as np
import json
from datetime import datetime
from datetime import timedelta

def preprocess():
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
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - activities_with_zones to data_processed/activities_with_zones.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # Reduce data for initial exploration
    reduced_expl = activities_with_zones.copy()
    reduced_expl = reduced_expl[['name', 'sport_type', 'start_date_local', 'location_country', 'distance', 
                                'moving_time', 'total_elevation_gain', 'kudos_count', 'athlete_count', 'average_speed',
                                'average_temp', 'average_watts', 'weighted_average_watts', 'average_heartrate',
                                'pr_count', 'total_photo_count', 'suffer_score']]

    print("------------------------------------- reduced_expl - head ---------------------------------------------")
    print(reduced_expl.head())
    print("-------------------------------------------------------------------------------------------------------")

    # get only ride data
    reduced_rides = reduced_expl[reduced_expl['sport_type'] == 'Ride'].drop(columns=['sport_type'])

    # Convert start_date_local to datetime object
    # Define the format of the datetime string
    datetime_format = "%Y-%m-%dT%H:%M:%SZ"

    # Parse the datetime string into a datetime object
    reduced_rides['start_date_local'] = reduced_rides['start_date_local'].apply(lambda x : datetime.strptime(x, datetime_format))

    # convert distance from meters to km
    reduced_rides['distance'] = reduced_rides['distance'].apply(lambda x : round(x / 1000, 3))

    # convert moving time from seconds to timedelta
    reduced_rides['moving_time'] = reduced_rides['moving_time'].apply(lambda x : timedelta(seconds=x))

    # convert avg speed from m/s to km/h
    reduced_rides['average_speed'] = reduced_rides['average_speed'].apply(lambda x : round(x / 10 * 36, 3))

    print("------------------------------------- reduced_rides - head --------------------------------------------")
    print(reduced_rides.head())
    print("-------------------------------------------------------------------------------------------------------")

    # saving current state - reduced_rides_expl - to csv as checkpoint
    reduced_rides.to_csv('data_processed/reduced_rides_expl.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - activities_with_zones reduced_rides to data_processed/reduced_rides_expl.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # combine ftp data with zone data, create copy and add column with nans
    activities_zones_ftp_full_data = activities_with_zones.copy()
    activities_zones_ftp_full_data['ftp'] = np.nan
    
    # read power stream of all activities
    power_stream_filepath = 'data_original/strava_power_streams_per_activity.csv'
    power_stream = pd.read_csv(power_stream_filepath)

    print("------------------------------------- power_stream - head ---------------------------------------------")
    print(power_stream.head(1))
    print("-------------------------------------------------------------------------------------------------------")
    
    # function to calculate ftp by running sliding window average
    # get average of window_size, preferably 1200 and multiply by 0.95 to get ftp (estimate 1 hour power) from 20 min average power
    def sliding_window_ftp(arr, window_size=1200):
        max_20_min_power = 0
        a_len = len(arr)
        if a_len < window_size:
            return 0
        cum_power = 0
        
        for i in range(window_size):
            cum_power += arr[i]

        max_20_min_power = cum_power / window_size
        left = 0
        right = window_size

        while right < a_len:
            cum_power -= arr[left]
            cum_power += arr[right]
            left += 1
            right += 1
            cur_average = cum_power / a_len
            if cur_average > max_20_min_power:
                max_20_min_power = cur_average

        return max_20_min_power * 0.95
    
    seconds_in_20_mins = 20 * 60

    # iterate through power_stream, parse data, calculate 20 min average, get ftp per ride and add to dataset
    for idx, row in power_stream.iterrows():
        id = row.loc['id']
        watts = row.loc['watts']
        if type(watts) == type(.1):
            continue
        cleaned_watts = watts.replace("'", '"').replace('None', '0')
        parsed_watts = json.loads(cleaned_watts)['data']
        ftp_based_on_ride = sliding_window_ftp(parsed_watts, seconds_in_20_mins)
        activities_zones_ftp_full_data.loc[activities_zones_ftp_full_data['id'] == id, 'ftp'] = ftp_based_on_ride

    # save to file
    activities_zones_ftp_full_data.to_csv('data_processed/activities_zones_ftp_full_data.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - activities_zones_ftp_full_data to data_processed/activities_zones_ftp_full_data.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # reduce zones ftp data
    full_data_only_rides = activities_zones_ftp_full_data[activities_zones_ftp_full_data['sport_type'] == 'Ride']
    zones_ftp_reduced = full_data_only_rides[['distance', 'moving_time', 'start_date_local', 'kilojoules', 'average_heartrate', 'HR Zone 1', 'HR Zone 2', 'HR Zone 3', 'HR Zone 4', 'HR Zone 5', 'Power Zone 1', 'Power Zone 2', 'Power Zone 3', 'Power Zone 4', 'Power Zone 5', 'Power Zone 6', 'Power Zone 7', 'Power Zone 8', 'Power Zone 9', 'Power Zone 10', 'Power Zone 11', 'ftp']]
    zones_ftp_reduced.to_csv('data_processed/zones_ftp_reduced.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_reduced to data_processed/zones_ftp_reduced.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # power focused data
    zones_ftp_power_with_na = zones_ftp_reduced[['distance', 'moving_time', 'start_date_local', 'kilojoules', 'Power Zone 1', 'Power Zone 2', 'Power Zone 3', 'Power Zone 4', 'Power Zone 5', 'Power Zone 6', 'Power Zone 7', 'Power Zone 8', 'Power Zone 9', 'Power Zone 10', 'Power Zone 11', 'ftp']]
    zones_ftp_power = zones_ftp_power_with_na.dropna(subset=['kilojoules'])
    zones_ftp_power.to_csv('data_processed/zones_ftp_power.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_power to data_processed/zones_ftp_power.csv')
    print("-------------------------------------------------------------------------------------------------------")

    zones_ftp_hr_with_na = zones_ftp_reduced[['distance', 'moving_time', 'start_date_local', 'average_heartrate', 'HR Zone 1', 'HR Zone 2', 'HR Zone 3', 'HR Zone 4', 'HR Zone 5', 'ftp']]
    zones_ftp_hr = zones_ftp_hr_with_na.dropna(subset=['average_heartrate'])
    zones_ftp_hr.to_csv('data_processed/zones_ftp_hr.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_hr to data_processed/zones_ftp_hr.csv')
    print("-------------------------------------------------------------------------------------------------------")

    zones_ftp_power_hr = zones_ftp_reduced.dropna(subset=['average_heartrate', 'kilojoules'])
    zones_ftp_power_hr.to_csv('data_processed/zones_ftp_power_hr.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_power_hr to data_processed/zones_ftp_power_hr.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # aggregate data based on year and month, get max ftp for each month and sum other fields
    zones_ftp_power_month = zones_ftp_power.copy()
    zones_ftp_power_month['month'] = pd.to_datetime(zones_ftp_power_month['start_date_local']).dt.month_name()
    zones_ftp_power_month['year'] = pd.to_datetime(zones_ftp_power_month['start_date_local']).dt.year
    zones_ftp_power_agg_with_na = zones_ftp_power_month.groupby(['year', 'month']).agg({
        'distance': 'sum',
        'moving_time': 'sum',
        'kilojoules': 'sum',
        'Power Zone 1': 'sum',
        'Power Zone 2': 'sum',
        'Power Zone 3': 'sum',
        'Power Zone 4': 'sum',
        'Power Zone 5': 'sum',
        'Power Zone 6': 'sum',
        'Power Zone 7': 'sum',
        'Power Zone 8': 'sum',
        'Power Zone 9': 'sum',
        'Power Zone 10': 'sum',
        'Power Zone 11': 'sum',
        'ftp': 'max'
    }).reset_index()
    zones_ftp_power_agg = zones_ftp_power_agg_with_na.dropna().drop(columns=['year', 'month'])
    zones_ftp_power_agg.to_csv('data_processed/zones_ftp_power_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_power_agg to data_processed/zones_ftp_power_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # aggregate monthly hr data, similar as before
    zones_ftp_hr_month = zones_ftp_hr.copy()
    zones_ftp_hr_month['month'] = pd.to_datetime(zones_ftp_hr_month['start_date_local']).dt.month_name()
    zones_ftp_hr_month['year'] = pd.to_datetime(zones_ftp_hr_month['start_date_local']).dt.year
    zones_ftp_hr_agg_with_na = zones_ftp_hr_month.groupby(['year', 'month']).agg({
        'distance': 'sum',
        'moving_time': 'sum',
        'average_heartrate': 'sum',
        'HR Zone 1': 'sum',
        'HR Zone 2': 'sum',
        'HR Zone 3': 'sum',
        'HR Zone 4': 'sum',
        'HR Zone 5': 'sum',
        'ftp': 'max'
    }).reset_index()
    zones_ftp_hr_agg = zones_ftp_hr_agg_with_na.dropna().drop(columns=['year', 'month'])
    zones_ftp_hr_agg.to_csv('data_processed/zones_ftp_hr_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_hr_agg to data_processed/zones_ftp_hr_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # aggregate power + hr data
    zones_ftp_power_hr_month = zones_ftp_power_hr.copy()
    zones_ftp_power_hr_month['month'] = pd.to_datetime(zones_ftp_power_hr_month['start_date_local']).dt.month_name()
    zones_ftp_power_hr_month['year'] = pd.to_datetime(zones_ftp_power_hr_month['start_date_local']).dt.year
    zones_ftp_power_hr_agg_with_na = zones_ftp_power_hr_month.groupby(['year', 'month']).agg({
        'distance': 'sum',
        'moving_time': 'sum',
        'average_heartrate': 'sum',
        'HR Zone 1': 'sum',
        'HR Zone 2': 'sum',
        'HR Zone 3': 'sum',
        'HR Zone 4': 'sum',
        'HR Zone 5': 'sum',
        'kilojoules': 'sum',
        'Power Zone 1': 'sum',
        'Power Zone 2': 'sum',
        'Power Zone 3': 'sum',
        'Power Zone 4': 'sum',
        'Power Zone 5': 'sum',
        'Power Zone 6': 'sum',
        'Power Zone 7': 'sum',
        'Power Zone 8': 'sum',
        'Power Zone 9': 'sum',
        'Power Zone 10': 'sum',
        'Power Zone 11': 'sum',
        'ftp': 'max'
    }).reset_index()
    zones_ftp_power_hr_agg = zones_ftp_power_hr_agg_with_na.dropna().drop(columns=['year', 'month'])
    zones_ftp_power_hr_agg.to_csv('data_processed/zones_ftp_power_hr_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_power_hr_agg to data_processed/zones_ftp_power_hr_agg.csv')
    print("-------------------------------------------------------------------------------------------------------")

    # Function to perform data augmentation
    def augment_data(dataframe, num_augmentations=5, noise_factor=0.1):
        augmented_dataframes = dataframe.copy()
        
        for _ in range(num_augmentations):
            augmented_sample = dataframe.copy()
            for column in dataframe.columns:
                if column != 'ftp':
                    augmented_sample[column] *= np.random.uniform(1 - noise_factor, 1 + noise_factor)
            augmented_dataframes = pd.concat([augmented_dataframes, augmented_sample], ignore_index=True)
        return augmented_dataframes.reset_index(drop=True)

    zones_ftp_power_agg_augmented = augment_data(zones_ftp_power_agg, num_augmentations=3)
    zones_ftp_power_agg_augmented.to_csv('data_processed/zones_ftp_power_agg_augmented.csv')
    zones_ftp_hr_agg_augmented = augment_data(zones_ftp_hr_agg, num_augmentations=3)
    zones_ftp_hr_agg_augmented.to_csv('data_processed/zones_ftp_hr_agg_augmented.csv')
    zones_ftp_power_hr_agg_augmented = augment_data(zones_ftp_power_hr_agg, num_augmentations=3)
    zones_ftp_power_hr_agg_augmented.to_csv('data_processed/zones_ftp_power_hr_agg_augmented.csv')
    print("-------------------------------------------------------------------------------------------------------")
    print('Exported current state - zones_ftp_power_agg_augmented to data_processed/zones_ftp_power_agg_augmented.csv')
    print('Exported current state - zones_ftp_hr_agg_augmented to data_processed/zones_ftp_hr_agg_augmented.csv')
    print('Exported current state - zones_ftp_power_hr_agg_augmented to data_processed/zones_ftp_power_hr_agg_augmented.csv')
    print("-------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    preprocess()