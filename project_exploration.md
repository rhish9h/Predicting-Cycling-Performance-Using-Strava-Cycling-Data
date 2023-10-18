#### SER594: Exploratory Data Munging and Visualization
#### Quest for improvement: a data driven search for cycling performance improvement (title)
#### Rhishabh Suhas Hattarki (author)
#### 18 October 2023 (date)

## Basic Questions
**Dataset Author(s):** Rhishabh Suhas Hattarki

**Dataset Construction Date:** 17 October 2023

**Dataset Record Count:** 1601

**Dataset Field Meanings:** 

strava_activities.csv:

resource_state - Resource state, indicates level of detail. Possible values: 1 -> "meta", 2 -> "summary", 3 -> "detail"  
athlete - An instance of MetaAthlete {'id': '{id}', 'resource_state': '{resource_state}'}  
name - The name of the activity  
distance - The activity's distance, in meters  
moving_time - The activity's moving time, in seconds  
elapsed_time - The activity's elapsed time, in seconds  
total_elevation_gain - The activity's total elevation gain  
type - Activity type. Deprecated. Prefer to use sport_type  
sport_type - An instance of SportType (Enum of different sports)  
workout_type - The activity's workout type  
id - The unique identifier of the activity  
start_date - The time at which the activity was started  
start_date_local - The time at which the activity was started in the local timezone  
timezone - The timezone of the activity  
utc_offset - The difference in hours and minutes between Coordinated Universal Time (UTC) and local solar time, at a particular place  
location_city - The city of activity  
location_state - The state of activity  
location_country - The country of activity  
achievement_count - The number of achievements gained during this activity  
kudos_count - The number of kudos given for this activity  
comment_count - The number of comments for this activity  
athlete_count - The number of athletes for taking part in a group activity  
photo_count - The number of Instagram photos for this activity  
map - An instance of PolylineMap  
trainer - Whether this activity was recorded on a training machine  
commute - Whether this activity is a commute  
manual - Whether this activity was created manually  
private - Whether this activity is private  
visibility - Who the activity is visible to  
flagged - Whether this activity is flagged  
gear_id - The id of the gear for the activity  
start_latlng - An instance of LatLng  
end_latlng - An instance of LatLng  
average_speed - The activity's average speed, in meters per second  
max_speed - The activity's max speed, in meters per second  
average_cadence - The activity's average cadence in rpm  
average_temp - The activity's average temperature in celsius  
average_watts - Average power output in watts during this activity. Rides only  
max_watts - Rides with power meter data only  
weighted_average_watts - Similar to Normalized Power. Rides with power meter data only  
kilojoules - The total work done in kilojoules during this activity. Rides only  
device_watts - Whether the watts are from a power meter, false if estimated  
has_heartrate - Whether activity has heartrate  
average_heartrate - The heart heart rate of the athlete during this activity  
max_heartrate - The maximum heart rate of the athlete during this activity  
heartrate_opt_out - Whether athlete chose to opt out of heartrate  
display_hide_heartrate_option - Whether athlete chose to show heartrate  
elev_high - The activity's highest elevation, in meters  
elev_low - The activity's lowest elevation, in meters  
upload_id - The identifier of the upload that resulted in this activity  
upload_id_str - The unique identifier of the upload in string format  
external_id - The desired external identifier of the resulting activity  
from_accepted_tag - No idea  
pr_count - Number of personal records achieved in the activity  
total_photo_count - The number of Instagram and Strava photos for this activity  
has_kudoed - Whether the logged-in athlete has kudoed this activity  
suffer_score - Score assigned by Strava based on the intensity and difficulty of activity  

strava_zones_per_activity.csv

score - Relative effort score based on heart rate  
distribution_buckets - List of buckets with min, max and time spent in zone  
type - Type of zones (heartrate/power)  
resource_state - Resource state, indicates level of detail. Possible values: 1 -> "meta", 2 -> "summary", 3 -> "detail"  
sensor_based - Whether zones are sensor based  
points - Points given by Strava  
custom_zones - Whether zones are custom  
id - Unique id of activity

**Dataset File Hash(es):**  
MD5 (strava_activities.csv) = d10b6bef9919938f089d40a9da207572  
MD5 (strava_zones_per_activity.csv) = 4de2a92cceafa3e5f300b52bafbecd92

## Interpretable Records
### Record 1
**Raw Data:** TODO

Interpretation:** TODO

### Record 2
**Raw Data:** TODO

**Interpretation:** TODO

## Background Domain Knowledge
TODO

## Data Transformation
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)