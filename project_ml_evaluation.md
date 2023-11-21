#### SER594: Machine Learning Evaluation
#### Predicting cycling performance using Strava cycling data (title)
#### Rhishabh Suhas Hattarki (author)
#### 20 November 2023 (date)

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error

**Choice Justification:** Mean squared error is the sum of squares of differences between the actual value, ftp in our case and the predicted ftp. This tells how far off our prediction was in terms of square of ftp thereby giving a goal for minimizing this error metric to get a better performing model. This works well with the continuous data in my dataset. Hence it is justified to be used here.

**Interpretation:** A lower mean squared error means that the model is closely fit and a higher MSE means that the model is not as closely fit. Since it gives errors in terms of squares of ftp, an MSE of 1000 is high as on average it is root(1000) ~ 31.6 watts away from actual ftp. In general my ftp ranges in the 200-300 watts range, 31.6 watts can be roughly 10-15% of performance difference which is huge. However a lower MSE like 400 is relatively a more desirable outcome as it is only ~20 watts off, still high but relatively better.

### Metric 2
**Name:** R squared Error

**Choice Justification:** R squared is another error metric, but this one can tell how much of the variability in the dependent variable, ftp in our case can be explained by the model, ie the patterns in the independent variables. This gives a range between 0 and 1 which makes it a lot easier to interpret the results as it is uniform and not dependent on the scale of the dependent variable. This makes it a justified evaluation metric.

**Interpretation:** An R squared error of 0 indicates that the model does not explain any variability in ftp (dependent variable) and an R2 error of 1 indicates that model perfectly predicts the ftp. In our case models with higher R2 scores like 0.75 are better performing than the lower ones like 0.25.

## Alternative Models

I had a total of 18 models, since only 3 need to be mentioned, I will explain the top 3 best performing alternative models.

### Alternative 1
**Construction:** zones_ftp_power_hr_agg, Lasso : This model was constructed using a subset of data that consists of both power and heart rate data - total work done in kilojoules, time spent in 11 power zones, average ride heart rate along with time spent in 5 heart rate zones. The ML model used was Lasso regression.

**Evaluation:** The mean squared error was 382.7173371675 and the R squared error was 0.744259593. (compared to baseline Linear Regression on only power data MSE: 1065.7726195411, R2: 0.2504477979)

### Alternative 2
**Construction:** zones_ftp_power_hr_agg, Ridge : This model was constructed using a subset of data that consists of both power and heart rate data - total work done in kilojoules, time spent in 11 power zones, average ride heart rate along with time spent in 5 heart rate zones. The ML model used was Ridge regression.

**Evaluation:** The mean squared error was 503.7133687483 and the R squared error was 0.6634072997. (compared to baseline Linear Regression on only power data MSE: 1065.7726195411, R2: 0.2504477979)

### Alternative 3
**Construction:** zones_ftp_power_hr_agg_augmented, Ridge : This model was constructed using a subset of data that consists of both power and heart rate data - total work done in kilojoules, time spent in 11 power zones, average ride heart rate along with time spent in 5 heart rate zones. The ML model used was Ridge regression. Moreover, this consisted of augmented data, it had about 4 times the data of other non augmented datasets. This was additional data added in augmentation process with a noise factor of 0.1.

**Evaluation:** The mean squared error was 512.0358563414 and the R squared error was 0.7544735501. (compared to baseline Linear Regression on only power data MSE: 1065.7726195411, R2: 0.2504477979)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)

## Best Model

**Model:** zones_ftp_power_hr_agg, Ridge : This model (explained above) was best performing. With an MSE of ~382.7, it was on average off by 19.56 watts from the actual ftp.