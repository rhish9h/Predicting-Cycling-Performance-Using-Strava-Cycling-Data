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
workout_type - The activity's workout type 'workout_type' : {
  'run' : {
    '0' : 'None',
    '1' : 'Race',
    '3' : 'Workout',
    '2' : 'Long Run'
  }
  'ride' : {
    '10' : 'None',
    '11' : 'Race',
    '12' : 'Workout'
  }
}  
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
**Raw Data:**

strava_activities.csv

| resource\_state | athlete | name | distance | moving\_time | elapsed\_time | total\_elevation\_gain | type | sport\_type | workout\_type | id | start\_date | start\_date\_local | timezone | utc\_offset | location\_city | location\_state | location\_country | achievement\_count | kudos\_count | comment\_count | athlete\_count | photo\_count | map | trainer | commute | manual | private | visibility | flagged | gear\_id | start\_latlng | end\_latlng | average\_speed | max\_speed | average\_cadence | average\_temp | average\_watts | max\_watts | weighted\_average\_watts | kilojoules | device\_watts | has\_heartrate | average\_heartrate | max\_heartrate | heartrate\_opt\_out | display\_hide\_heartrate\_option | elev\_high | elev\_low | upload\_id | upload\_id\_str | external\_id | from\_accepted\_tag | pr\_count | total\_photo\_count | has\_kudoed | suffer\_score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | "\{'id': 3506416, 'resource\_state': 1\}" | "Feel the fatigue, need rest" | 63539\.8 | 8189 | 8382 | 131\.0 | Ride | Ride | 10\.0 | 10057164887 | 2023\-10\-17T17:00:06Z | 2023\-10\-17T10:00:06Z | \(GMT\-07:00\) America/Phoenix | \-25200\.0 |  |  | United States | 10 | 17 | 0 | 1 | 0 | "\{'id': 'a10057164887', 'summary\_polyline': 'qe~jEzubjTLw@jADLdAdCxDpBeBTmAnBAEd\\\\l@\`FHfMc@n@oBHSfARjR~@nGGnEyAv@Yz@mBPiOc@i\\\\\\\\MRGnRyW^qHfHoAzCcBp@GnCa@tA`@dCSvI\]bCVxDy@bIQtIiFzt@s@jDm@xIJdDg@vNT~Np@rKxCxSpEjPDfBp@`DlE~Nt@bA`B`FlO~i@`DrO`BlPp@nVt@bLxBtNzOxh@`Ydq@zElN~AtCx@l@LdDhD`VIxIiBrAQh@jAxMm@fRb@bB\[~GEvSgAnFn@jGa@zNaBfJs@fOuAdGwAtDQ~BLvMSzFeFpL\_AfDo@zG\[rLy@bLe@`T\\\\lE~@fCqB~XnBlCyAeBOi@nB\_YaAaDW\_Ef@oTx@oKXeLr@oHbAmD`FgLNmCA\_TpDwMr@sOdBgJ^aOo@uFdAeGBmS\\\\cHc@aBn@uQoAgNNi@lBqAHwImD\}UQoD\_Ao@uAoC\_EqLwYir@aPgi@\_C\}OQeG\_@\_Cq@\}VkC\}TsBoJmO\{i@eBgFm@y@gFuQa@cB?sAwEaQaCcPy@uKWuJBeL`@kIOoBp@eKr@cDvFey@?aDv@mKSgDn@gI?mDc@\{Ah@qBBaJIdJk@\|A`@nBOfJ\_@lCXpDu@dH\_@jMaF~r@q@bDo@rJNxB\_@`HCrNpAzUlB~MbCrKjB~FB\|Al@vCpEdOr@dAbBbF`Rvq@rAxHpAdMv@dXt@jL`CrOlPxi@hYrq@`EvLvAjC~@r@HtCjDtVC`I\_CjChAzMk@hRb@vA\]`HCtSgAxFl@fG\_@pNeBzJq@hOyA`GiAlCUnBEjViHnRq@bH\]`My@`La@tSZdE`AlCqBpXNr@r@Zd@hAPOuBaCpB\_Y\}@iC\[aE`@cTz@eLZoLp@gHdH\}Q@eUNoBlDsMr@gOdBkJ`@cOo@wFfAmGBqSZwGc@wAl@cRkAcNNk@jBsAFaJmDyUOcD\_As@sAmCqEuMaYaq@\_P\}h@eCmPSeG\_@gCs@\}VmAaMmAyH\{Rct@kCmGsEoOq@yCA\}AsCqJ\{C\_P\{@uHy@qOKmLh@wMQwBr@mKp@yC`Fur@b@iNuO\}B\|@g\]A\}E\_@aEPeCf@\_`@oBqSdBNzBc@bAiEQiAmHJ^\|IfBbRm@`SB~JSrCf@hIy@d`@lOfBp@uFS\}D^mCN\}Ic@mBd@\_B?iClBw@hAiCdBgApC\}DjA\_@pWYRa@A\{QPWx`@EdL^^kAnAu@b@kEm@cHOaTd@m@dBARi@BoMm@yEHyVq@MiC\|C', 'resource\_state': 2\}" | False | False | False | False | everyone | False | b12532853 | "\[33\.419589484110475, \-111\.92323436960578\]" | "\[33\.41942980885506, \-111\.92315675318241\]" | 7\.759 | 13\.21 | 88\.4 | 32\.0 | 155\.9 | 723\.0 | 174\.0 | 1276\.9 | True | True | 152\.1 | 187\.0 | False | True | 361\.2 | 316\.8 | 10774879897\.0 | 10774879897 | garmin\_ping\_300060328822 | False | 2 | 1 | False | 176\.0 |

strava_zones_per_activity.csv

|  | 0 | 1 | 2 |
|---|---|---|---|
| 0 | "\{'score': 176\.0, 'distribution\_buckets': \[\{'min': 0, 'max': 115, 'time': 125\}, \{'min': 115, 'max': 152, 'time': 4257\}, \{'min': 152, 'max': 170, 'time': 2782\}, \{'min': 170, 'max': 189, 'time': 1025\}, \{'min': 189, 'max': \-1, 'time': 0\}\], 'type': 'heartrate', 'resource\_state': 3, 'sensor\_based': True, 'points': 22, 'custom\_zones': False\}" | "\{'distribution\_buckets': \[\{'max': 0, 'min': 0, 'time': 618\}, \{'max': 50, 'min': 0, 'time': 127\}, \{'max': 100, 'min': 50, 'time': 738\}, \{'max': 150, 'min': 100, 'time': 1868\}, \{'max': 200, 'min': 150, 'time': 3179\}, \{'max': 250, 'min': 200, 'time': 951\}, \{'max': 300, 'min': 250, 'time': 564\}, \{'max': 350, 'min': 300, 'time': 88\}, \{'max': 400, 'min': 350, 'time': 29\}, \{'max': 450, 'min': 400, 'time': 7\}, \{'max': \-1, 'min': 450, 'time': 20\}\], 'type': 'power', 'resource\_state': 3, 'sensor\_based': True\}" | \{'id': 10057164887\} |

**Interpretation:** 

strava_activities.csv:

resource_state - 2 means it is summary level data  
athlete - it's my athlete id with resource state 2 which is summary level  
name - I felt fatigued that day  
distance - I rode ~63km that day   
moving_time - I rode for ~2hr 16min  
elapsed_time - The total time including breaks was ~2hr 20min  
total_elevation_gain - Total elevation gain was 131m  
type - Type of activity was ride  
sport_type - Type of sport was ride  
workout_type - The workout was a normal ride, not a race  
id - The unique identifier of the activity  
start_date - The ride started at 5pm UTC on 17 October 2023  
start_date_local - The ride started at 10am AZ time on 17 October 2023  
timezone - The timezone of the activity was Phoenix AZ time  
utc_offset - The time in question was 25,200 seconds behind Coordinated Universal Time (UTC)  
location_city - Blank  
location_state - Blank  
location_country - The country of activity was USA  
achievement_count - The number of achievements gained during this activity was 10  
kudos_count - The number of kudos given for this activity was 17  
comment_count - The number of comments for this activity was 0  
athlete_count - The number of athletes for taking part in a group activity was 1, solo ride  
photo_count - The number of Instagram photos for this activity was 0  
map - An instance of PolylineMap, can be deciphered using Google's Polyline tool, shows a map of the ride  
trainer - Not a trainer ride  
commute - Not a commute  
manual - Not added manually  
private - Not private  
visibility - Visible to everyone  
flagged - Not flagged  
gear_id - The id of the gear for the activity  
start_latlng - That's where my ride started  
end_latlng - That's where my ride ended  
average_speed - Average speed was 27.9kph  
max_speed - Max speed was 47.6kph  
average_cadence - Average cadence was 88.4  
average_temp - The average temperature in celsius was 32  
average_watts - Average power output in watts during this activity was 155.9  
max_watts - Max power was 723w  
weighted_average_watts - Weighter average power was 174w  
kilojoules - The total work done in kilojoules during this activity was 1276.9  
device_watts - Power data was from a powermeter  
has_heartrate - Activity has heartrate  
average_heartrate - The heart heart rate of the athlete during this activity was 152.1  
max_heartrate - The maximum heart rate of the athlete during this activity was 187  
heartrate_opt_out - Did not choose to opt out of heartrate  
display_hide_heartrate_option - Chose to show heartrate  
elev_high - The activity's highest elevation, in meters was 361.2  
elev_low - The activity's lowest elevation, in meters was 316.  
upload_id - The identifier of the upload that resulted in this activity  
upload_id_str - The unique identifier of the upload in string format  
external_id - The desired external identifier of the resulting activity  
from_accepted_tag - No idea  
pr_count - Number of personal records achieved in the activity was 2  
total_photo_count - The number of Instagram and Strava photos for this activity was 1  
has_kudoed - It's my own activity, I did not kudo myself  
suffer_score - Score assigned by Strava based on the intensity and difficulty of activity was 176  

strava_zones_per_activity.csv

score - Relative effort score based on heart rate was 176  
distribution_buckets -  
Heart Rate -  
Zone 1: [0-115]: 2min 5sec  
Zone 2: [115-152]: 1hr 10min 57sec  
Zone 3: [152-170]: 46min 22sec  
Zone 4: [170-189]: 17min 5sec  
Zone 5: [>189]: 0min  
Power -  
[0-0]: 10 min 18 sec  
[0-50]: 2 min 7 sec  
[50-100]: 12 min 18 sec  
[100-150]: 31 min 8 sec  
[150-200]: 52 min 59 sec  
[200-250]: 15 min 51 sec  
[250-300]: 9 min 24 sec  
[300-350]: 1 min 28 sec  
[350-400]: 29 sec  
[400-450]: 7 sec  
[450<]: 20 sec  
type - Type of zones - both hr and power available  
resource_state - Detail data  
sensor_based - yes, it's sensor based  
points - Points given by Strava was 22  
custom_zones - Not custom  
id - Unique id of activity

### Record 2
**Raw Data:**

strava_activities.csv

| resource\_state | athlete | name | distance | moving\_time | elapsed\_time | total\_elevation\_gain | type | sport\_type | workout\_type | id | start\_date | start\_date\_local | timezone | utc\_offset | location\_city | location\_state | location\_country | achievement\_count | kudos\_count | comment\_count | athlete\_count | photo\_count | map | trainer | commute | manual | private | visibility | flagged | gear\_id | start\_latlng | end\_latlng | average\_speed | max\_speed | average\_cadence | average\_temp | average\_watts | max\_watts | weighted\_average\_watts | kilojoules | device\_watts | has\_heartrate | average\_heartrate | max\_heartrate | heartrate\_opt\_out | display\_hide\_heartrate\_option | elev\_high | elev\_low | upload\_id | upload\_id\_str | external\_id | from\_accepted\_tag | pr\_count | total\_photo\_count | has\_kudoed | suffer\_score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | "\{'id': 3506416, 'resource\_state': 1\}" | AZ State ITT \- 7th/11 in Men Merckx \- destroyed by the headwind | 39964\.1 | 4020 | 4020 | 42\.0 | Ride | Ride | 11\.0 | 9912737242 | 2023\-09\-24T14:45:58Z | 2023\-09\-24T07:45:58Z | \(GMT\-07:00\) America/Phoenix | \-25200\.0 |  |  | United States | 0 | 26 | 6 | 3 | 0 | "\{'id': 'a9912737242', 'summary\_polyline': 'ykgfEhyzfTbUw\\\\xAsB~AqB~\`@se@j\_@qc@pCwCpDeDdiAc\}@~L\}Jpi@ob@rO\_MbHsFrIaHxk@od@tDuCfLgJxMgKpJyHbKaIz\[gWnAaAdAs@lAo@jCoAdAq@\|I\_HlQqNbA\}@fBkB~BuCd@g@\|A\{AnDqCbEwCrPuMnWwShM\{J~c@a^rXiTrIaHhY\}T\|VeS\|KuIvl@me@vEoDrQuNzDyC`r@wi@vFqEb^\}XzEyDlVmRdBgAbFkCtCmBbZoUJOAECAEB\_\\\\dWwChBmDhBkAp@gAx@cDfCql@de@o`@\|ZeVpRaLvIaw@~m@yAfAkM`K\{RrO\_F~DyB`BwYjUufAd\{@\{TdQiB\|A\}GjFyYpU\{EtDoBpAmCpBkB~Ao@l@o@t@sBjCsCrC\}StPaHlF\{@h@qEzBwBvAgCnB\{n@dg@\}XrTkH~FuIxGqgBxvAgOnLiMdK\}SjP\}l@te@oDdDuCzCsSdVol@pr@aC~CmBnCkSnZ', 'resource\_state': 2\}" | False | False | False | False | everyone | False | b12532853 | "\[32\.64717631973326, \-111\.38980829156935\]" | "\[32\.647236585617065, \-111\.38979689218104\]" | 9\.941 | 15\.096 | 86\.7 | 22\.0 | 249\.9 | 731\.0 | 249\.0 | 1004\.5 | True | True | 175\.6 | 185\.0 | False | True | 583\.6 | 536\.4 | 10624071939\.0 | 10624071939 | garmin\_ping\_296207949248 | False | 0 | 6 | False | 211\.0 |

strava_zones_per_activity.csv

|  | 0 | 1 | 2 |
|---|---|---|---|
| 17 | "\{'score': 211\.0, 'distribution\_buckets': \[\{'min': 0, 'max': 115, 'time': 0\}, \{'min': 115, 'max': 152, 'time': 28\}, \{'min': 152, 'max': 170, 'time': 150\}, \{'min': 170, 'max': 189, 'time': 3842\}, \{'min': 189, 'max': \-1, 'time': 0\}\], 'type': 'heartrate', 'resource\_state': 3, 'sensor\_based': True, 'points': 201, 'custom\_zones': False\}" | "\{'distribution\_buckets': \[\{'max': 0, 'min': 0, 'time': 12\}, \{'max': 50, 'min': 0, 'time': 0\}, \{'max': 100, 'min': 50, 'time': 1\}, \{'max': 150, 'min': 100, 'time': 12\}, \{'max': 200, 'min': 150, 'time': 83\}, \{'max': 250, 'min': 200, 'time': 2101\}, \{'max': 300, 'min': 250, 'time': 1645\}, \{'max': 350, 'min': 300, 'time': 116\}, \{'max': 400, 'min': 350, 'time': 26\}, \{'max': 450, 'min': 400, 'time': 17\}, \{'max': \-1, 'min': 450, 'time': 7\}\], 'type': 'power', 'resource\_state': 3, 'sensor\_based': True\}" | \{'id': 9912737242\} |

**Interpretation:**

strava_activities.csv:

resource_state - 2 means it is summary level data  
athlete - it's my athlete id with resource state 2 which is summary level  
name - I participated in the AZ State ITT championships that day  
distance - I rode ~40km that day   
moving_time - I rode for ~1hr 7min  
elapsed_time - The total time including breaks was ~1hr 7min  
total_elevation_gain - Total elevation gain was 42m  
type - Type of activity was ride  
sport_type - Type of sport was ride  
workout_type - The workout was bicycle race  
id - The unique identifier of the activity  
start_date - The ride started at 2.46pm UTC on 24 September 2023  
start_date_local - The ride started at 7.46am AZ time on 24 September 2023  
timezone - The timezone of the activity was Phoenix AZ time  
utc_offset - The time in question was 25,200 seconds behind Coordinated Universal Time (UTC)  
location_city - Blank  
location_state - Blank  
location_country - The country of activity was USA  
achievement_count - The number of achievements gained during this activity was 0  
kudos_count - The number of kudos given for this activity was 26  
comment_count - The number of comments for this activity was 6  
athlete_count - The number of athletes for taking part in a group activity was 3  
photo_count - The number of Instagram photos for this activity was 0  
map - An instance of PolylineMap, can be deciphered using Google's Polyline tool, shows a map of the ride  
trainer - Not a trainer ride  
commute - Not a commute  
manual - Not added manually  
private - Not private  
visibility - Visible to everyone  
flagged - Not flagged  
gear_id - The id of the gear for the activity  
start_latlng - That's where my ride started  
end_latlng - That's where my ride ended  
average_speed - Average speed was 35.8kph  
max_speed - Max speed was 54.3kph  
average_cadence - Average cadence was 86.7  
average_temp - The average temperature in celsius was 22  
average_watts - Average power output in watts during this activity was 249.9  
max_watts - Max power was 731w  
weighted_average_watts - Weighter average power was 249w  
kilojoules - The total work done in kilojoules during this activity was 1004.5  
device_watts - Power data was from a powermeter  
has_heartrate - Activity has heartrate  
average_heartrate - The heart heart rate of the athlete during this activity was 175.6  
max_heartrate - The maximum heart rate of the athlete during this activity was 185  
heartrate_opt_out - Did not choose to opt out of heartrate  
display_hide_heartrate_option - Chose to show heartrate  
elev_high - The activity's highest elevation, in meters was 583.6  
elev_low - The activity's lowest elevation, in meters was 536.4  
upload_id - The identifier of the upload that resulted in this activity  
upload_id_str - The unique identifier of the upload in string format  
external_id - The desired external identifier of the resulting activity  
from_accepted_tag - No idea  
pr_count - Number of personal records achieved in the activity was 0  
total_photo_count - The number of Instagram and Strava photos for this activity was 6  
has_kudoed - It's my own activity, I did not kudo myself  
suffer_score - Score assigned by Strava based on the intensity and difficulty of activity was 211  

strava_zones_per_activity.csv

score - Relative effort score based on heart rate was 211  
distribution_buckets -  
Heart Rate -  
Zone 1: [0-115]: 0min  
Zone 2: [115-152]: 28sec  
Zone 3: [152-170]: 2min 30sec  
Zone 4: [170-189]: 1hr 4min 2sec  
Zone 5: [>189]: 0min  
Power -  
[0-0]: 12 sec  
[0-50]: 0 sec  
[50-100]: 1 sec  
[100-150]: 12 sec  
[150-200]: 1 min 23 sec  
[200-250]: 35 min 1 sec  
[250-300]: 27 min 25 sec  
[300-350]: 1 min 56 sec  
[350-400]: 26 sec  
[400-450]: 17 sec  
[450<]: 7 sec  
type - Type of zones - both hr and power available  
resource_state - Detail data  
sensor_based - yes, it's sensor based  
points - Points given by Strava was 201  
custom_zones - Not custom  
id - Unique id of activity

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