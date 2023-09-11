#### SER594: Project Proposal
#### Quest for improvement: a data driven search for cycling performance improvement (title)
#### Rhishabh Suhas Hattarki (author)
#### 11 Sept 2023 (date)

Keywords: 

- cycling
- training
- performance improvement

Description: 

As a dedicated cyclist with over 7 years of activity logged on Strava, I've meticulously collected data using tools like heart rate monitors, power meters, and sensors. I've also engaged in max power tests and bike races to assess performance objectively. My project's objective is to identify which training methods have yielded the most significant performance improvements in cycling. Training styles can be categorized based on time spent in specific heart rate/power zones during a training cycle, and there is existing research on their effects. Performance improvement can be tracked using metrics like FTP (max power output in 1 hour). However, it's crucial to recognize that what works for one person may not work for another, emphasizing the need to understand what training approach suits an individual best.
The data I'll utilize is sourced from Strava, where I've consistently logged activities, through GPX files from my Garmin device. Strava provides developer APIs for data retrieval, allowing access to structured data such as duration, time spent in power/heart rate zones, and average power. However, some rides may have missing data due to absence of a heart rate belt or power meter, which presents some challenges in data handling. Nevertheless, there is a substantial amount of high-quality data available for analysis.

Intellectual Merit:

Individualized training approaches are essential because what works for one athlete may not be effective for others. Athletes should strive to identify the training methods that yield optimal results for them. Creating a tool to uncover these insights not only benefits the user but also empowers athletes across various disciplines to reach their full potential by enhancing their understanding of their training regimen.

Data Sourcing: 

Strava has a set of APIs (https://developers.strava.com/docs/reference/) that can be used to fetch all my data in the form of JSON objects. This can later be converted to excel sheets / any necessary format for processing. The APIs are also rate limited to 2000 requests per day, so data collection will have to be done with minimum errors to avoid repeated
requests.

Background Knowledge: 

Medhus, J. B. (n.d.). Basic Principles of cycling training for Beginners. Training4cyclists.com. https://www.training4cyclists.com/basic-principles-of-cycling-training/

Mead, B. (2023). A comparison of polarized, sweet spot, and pyramidal training. Fast Talk Laboratories. https://www.fasttalklabs.com/articles/a-comparison-of-polarized-sweet-spot-and-pyramidal-training/

Yeager, S. (2022, February 9). Your guide to the key cycling metrics that can make your rides better. Bicycling. https://www.bicycling.com/training/a38918736/cycling-metrics-guide/

Related Work:

Demosthenous, G., Kyriakou, M., & Vassiliades, V. (2022). Deep reinforcement learning for improving competitive cycling performance. Expert Systems With Applications, 203, 117311. https://doi.org/10.1016/j.eswa.2022.117311

Neal, C. M., Hunter, A. M., Brennan, L., O’Sullivan, A., Hamilton, D. L., De Vito, G., & Galloway, S. D. R. (2013). Six weeks of a polarized training-intensity distribution leads to greater physiological and performance adaptations than a threshold model in trained cyclists. Journal of Applied Physiology, 114(4), 461–471. https://doi.org/10.1152/japplphysiol.00652.2012
