#### SER594: Project Proposal
#### Predicting cycling performance using Strava cycling data (title)
#### Rhishabh Suhas Hattarki (author)
#### 30 October 2023 (date)

Keywords: 

- cycling training
- performance improvement
- Strava data analysis

Description: 

As a dedicated cyclist with over 7 years of activity logged on Strava, I've meticulously collected data using tools like heart rate monitors, power meters, and sensors. I've also engaged in max power tests and bike races to assess performance objectively. My project's objective is to identify which training methods have yielded the most significant performance improvements in cycling. Training styles can be categorized based on time spent in specific heart rate/power zones during a training cycle, and there is existing research on their effects. Performance improvement can be tracked using metrics like FTP (max power output in 1 hour). However, it's crucial to recognize that what works for one person may not work for another, emphasizing the need to understand what training approach suits an individual best.
The data I'll utilize is sourced from Strava, where I've consistently logged activities, through GPX files from my Garmin device. Strava provides developer APIs for data retrieval, allowing access to structured data such as duration, time spent in power/heart rate zones, and average power. However, some rides may have missing data due to absence of a heart rate belt or power meter, which presents some challenges in data handling. Nevertheless, there is a substantial amount of high-quality data available for analysis.

Research Questions:

- RO1: To describe the trends within the time spent in training zones over the duration of training periods.
- RO2: To describe the trends within the performance changes over the duration of training periods.
- RO3: To predict the value of functional threshold power (FTP) using the Strava data of the previous training block.
- RO4: To defend the model for performing the prediction of FTP in RO3.
- RO5: To evaluate the causal relationships implied by the RO3 model.

Intellectual Merit:

Developing a personalized training tool empowers athletes to identify optimal training methods for their individual needs. Predicting functional threshold power (FTP) from training data streamlines evaluation without the need for explicit testing, reducing stress and enabling cyclists to optimize their training. While Strava and add-on extensions offer basic data analysis, FTP prediction represents a novel contribution, filling a knowledge gap in the field.

Data Sourcing: 

I utilized Strava's comprehensive set of APIs (accessible at https://developers.strava.com/docs/reference/) to retrieve my personal detailed activity data, including time spent in specific training zones. To further enhance the depth of analysis, additional APIs can be used to access per-second ride data streams, enabling a more fine-grained examination of cycling performance.

Background Knowledge: 

- Medhus, J. B. (n.d.). Basic Principles of cycling training for Beginners. Training4cyclists.com. https://www.training4cyclists.com/basic-principles-of-cycling-training/

- Mead, B. (2023). A comparison of polarized, sweet spot, and pyramidal training. Fast Talk Laboratories. https://www.fasttalklabs.com/articles/a-comparison-of-polarized-sweet-spot-and-pyramidal-training/

- Yeager, S. (2022, February 9). Your guide to the key cycling metrics that can make your rides better. Bicycling. https://www.bicycling.com/training/a38918736/cycling-metrics-guide/

Related Work:

- Demosthenous, G., Kyriakou, M., & Vassiliades, V. (2022). Deep reinforcement learning for improving competitive cycling performance. Expert Systems With Applications, 203, 117311. https://doi.org/10.1016/j.eswa.2022.117311

- Neal, C. M., Hunter, A. M., Brennan, L., O’Sullivan, A., Hamilton, D. L., De Vito, G., & Galloway, S. D. R. (2013). Six weeks of a polarized training-intensity distribution leads to greater physiological and performance adaptations than a threshold model in trained cyclists. Journal of Applied Physiology, 114(4), 461–471. https://doi.org/10.1152/japplphysiol.00652.2012

- Anderson, R. (2023, January 16). Running Smart with Machine Learning and Strava - Towards Data Science. Medium. https://towardsdatascience.com/running-smart-with-machine-learning-and-strava-9ba186decde0

- Data mining in sporting activities created by sports trackers. (2013, August 1). IEEE Conference Publication | IEEE Xplore. https://ieeexplore.ieee.org/abstract/document/6724329

- Jobson, S. A., Passfield, L., Atkinson, G., Barton, G., & Scarf, P. (2009). The analysis and utilization of cycling training data. Sports Medicine, 39(10), 833–844. https://doi.org/10.2165/11317840-000000000-00000

- Kholkine, L., De Schepper, T., Verdonck, T., & Latré, S. (2020). A Machine learning approach for Road cycling race performance Prediction. In Communications in computer and information science (pp. 103–112). https://doi.org/10.1007/978-3-030-64912-8_9
