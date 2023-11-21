#### SER594: Experimentation
#### Predicting cycling performance using Strava cycling data (title)
#### Rhishabh Suhas Hattarki (author)
#### 20 November 2023 (date)


## Explainable Records
### Record 1
**Raw Data:** 
```
distance             25474.2
moving_time           4328.0
average_heartrate       97.7
HR Zone 1             2952.0
HR Zone 2             1376.0
HR Zone 3                0.0
HR Zone 4                0.0
HR Zone 5                0.0
kilojoules             441.8
Power Zone 1           854.0
Power Zone 2           282.0
Power Zone 3          1026.0
Power Zone 4          1100.0
Power Zone 5           673.0
Power Zone 6           267.0
Power Zone 7            75.0
Power Zone 8            28.0
Power Zone 9            17.0
Power Zone 10            3.0
Power Zone 11            3.0
```
Output:
```
predicted FTP: 100.85093211152602
actual FTP: 111.34633333333332
```

**Prediction Explanation:** The aggregate moving time for the month here is 4328 seconds which is only ~1.2 hours for the entire month. That means that I did not train as much in this month at all. The total kilojoules for the month was also only 441.8 which can be done in a single ride. Even the time spent in HR zones 3, 4, 5 is 0. Considering all these factors, it is expected to have a low performance as there was close to no training this month. Hence the lower predicted ftp of ~100.8 is justifiable. It is also close to the actual ftp.

### Record 2
**Raw Data:** 
```
distance             839311.4
moving_time          116537.0
average_heartrate      2069.3
HR Zone 1              7888.0
HR Zone 2             90335.0
HR Zone 3             10449.0
HR Zone 4              7851.0
HR Zone 5                14.0
kilojoules            17346.3
Power Zone 1          15105.0
Power Zone 2           3304.0
Power Zone 3          14513.0
Power Zone 4          21317.0
Power Zone 5          39142.0
Power Zone 6          10478.0
Power Zone 7           6281.0
Power Zone 8           3531.0
Power Zone 9           1220.0
Power Zone 10           633.0
Power Zone 11          1013.0
```

Output:
```
predicted FTP: 184.25025285603553
actual FTP: 180.31079166666663
```

**Prediction Explanation:** Here, the total moving time is 116537 which is ~32.37 hours for the month, which is a decent amount of training for a month, I have gone to 40-50 during heavy training months (for comparison). The amount of work done is also considerably higher, 17346.3 which is ~535.8 kj per hour on average for this month. There is a significant time spent in training in higher HR zones 3, 4, 5. So it is natural that the training will pay off and a higher ftp will be gained. It is evident from the fact that it predicted ~184 which is much higher than before and also is similar to the actual ftp.

## Interesting Features
### Feature A
**Feature:** TODO

**Justification:** TODO

### Feature B
**Feature:** TODO

**Justification:** TODO

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)