import pandas as pd

# Set the display options to show all columns
pd.set_option('display.max_columns', None)

# Prevent truncation of cell contents
pd.set_option('display.max_colwidth', None)

# read data from reduced rides csv
reduced_rides = pd.read_csv('data_processed/reduced_rides_expl.csv')

print("------------------------------------- reduced_rides - head --------------------------------------------")
print(reduced_rides.head())
print("-------------------------------------------------------------------------------------------------------")

quant_columns = ['distance', 'total_elevation_gain', 'average_speed']
quantitative = reduced_rides[quant_columns]

qual_columns = ['location_country', 'moving_time']
qualitative = reduced_rides[qual_columns]

# get summary of quantitative data
quant_summary = pd.DataFrame({
    'Column': [],
    'Min': [],
    'Median': [],
    'Max': []
})

for col in quant_columns:
    row = {
        'Column': col,
        'Min': reduced_rides[col].min(),
        'Median': reduced_rides[col].median(),
        'Max': reduced_rides[col].max()
    }
    quant_summary.loc[len(quant_summary)] = row

print("------------------------------------- Quant summary ---------------------------------------------------")
print(quant_summary)
print("-------------------------------------------------------------------------------------------------------")

# get summary of qualitative data
qual_summary = pd.DataFrame({
    'Column': [],
    'Category_cnt': [],
    'Most_freq': [],
    'Least_freq': []
})

for col in qual_columns:
    mode = reduced_rides[col].mode()
    
    row = {
        'Column': col,
        'Category_cnt': len(reduced_rides[col].unique()),
        'Most_freq': mode[0],
        'Least_freq': reduced_rides[col].value_counts().idxmin()
    }
    qual_summary.loc[len(qual_summary)] = row

print("------------------------------------- Qual summary ----------------------------------------------------")
print(qual_summary)
print("-------------------------------------------------------------------------------------------------------")

# write summary to text file
summary = 'Quantitative summary\n\n' + quant_summary.to_string() + '\n\nQualitative summary\n\n' + qual_summary.to_string()
with open('data_processed/summary.txt', 'w') as file:
    file.write(summary)