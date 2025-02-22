import pandas as pd
import matplotlib.pyplot as plt

def visualize():
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

    # get correlation between quantitative features
    import numpy as np
    correlation_matrix = quantitative.corr()
    cols = [col for col in correlation_matrix.columns]
    trunc_corr_matrix = [['Column'] + cols]

    for col in cols:
        trunc_corr_matrix.append([col])

    for i in range(len(cols)):
        for j in range(i+1):
            trunc_corr_matrix[i+1].append(correlation_matrix.iloc[i, j])

    pretty_corr_matrix = ''

    for row in trunc_corr_matrix:
        row_str = ''
        for col in row:
            row_str += f'{col:<25}'
        pretty_corr_matrix += row_str + '\n'

    print("------------------------------------- Correlation matrix ----------------------------------------------")
    print(pretty_corr_matrix)
    print("-------------------------------------------------------------------------------------------------------")

    # write correlation matrix to txt file
    with open('data_processed/correlations.txt', 'w') as file:
        file.write(pretty_corr_matrix)

    print("------------------------------------- Scatter plots ---------------------------------------------------")
    print('Plotting Scatter plots')
    print("-------------------------------------------------------------------------------------------------------")

    # Scatter plots of quantitative data 
    quant_len = len(quant_columns)

    for i in range(quant_len):
        first_col = quant_columns[i]
        
        for j in range(i+1, quant_len):
            second_col = quant_columns[j]
            plt.scatter(quantitative[first_col], quantitative[second_col], s=7)
            plt.xlabel(first_col)
            plt.ylabel(second_col)
            plt.title(f'Scatter plot {first_col} vs {second_col}')
            plt.show()

    print("------------------------------------- Histograms ------------------------------------------------------")
    print('Plotting Histograms')
    print("-------------------------------------------------------------------------------------------------------")

    # Plotting histograms of qualitative features

    # location_country
    plt.hist(qualitative['location_country'], bins=2, color='lightblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Location country')
    plt.ylabel('Number of rides in country')
    plt.title('Histogram of location country')
    plt.savefig('visuals/histogram_location_country.png')
    plt.show()

    # moving_time
    moving_time = qualitative['moving_time'].copy().sort_values()

    plt.hist(moving_time, bins=40, color='lightblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Moving time')
    plt.ylabel('Number of rides by moving time')
    plt.title('Histogram of Moving time')

    x_ticks = [time for i, time in enumerate(moving_time) if i % 50 == 0]
    x_labels = [time for i, time in enumerate(moving_time) if i % 50 == 0]
    plt.xticks(x_ticks, x_labels, rotation=90)
    plt.savefig('visuals/histogram_moving_time.png')
    plt.show()

    print("------------------------------------- Trends in performance changes -----------------------------------")
    print('Trends in performance changes')
    print("-------------------------------------------------------------------------------------------------------")

    # Plot the trend in performace change in terms of FTP per training block over time
    zones_ftp_power_hr_agg = pd.read_csv('data_processed/zones_ftp_power_hr_agg.csv')
    ftp_only = zones_ftp_power_hr_agg[['ftp']]
    # Smooth the line using a rolling mean
    ftp_only_smoothed = ftp_only['ftp'].rolling(window=3).mean()

    plt.plot(ftp_only_smoothed, linestyle='--', color='#F9968B', label='Smoothed FTP Trend')
    plt.plot(ftp_only['ftp'], marker='o', linestyle='-', color='#2CCED2', label='FTP Trend')
    plt.title('FTP Over Different Months')
    plt.xlabel('Month')
    plt.ylabel('FTP')
    plt.legend()
    plt.savefig('visuals/trend_ftp_over_months.png')
    plt.show()

    print("------------------------------------- Trends in time spent in zones -----------------------------------")
    print('Trends in time spent in zones')
    print("-------------------------------------------------------------------------------------------------------")

    hr_zones_pre_convert = zones_ftp_power_hr_agg[['HR Zone 1','HR Zone 2','HR Zone 3','HR Zone 4','HR Zone 5']]
    hr_zones_only = pd.DataFrame()
    hr_zones_only['HR Zone 1'] = hr_zones_pre_convert['HR Zone 1'] / 3600
    hr_zones_only['HR Zone 2'] = hr_zones_pre_convert['HR Zone 2'] / 3600
    hr_zones_only['HR Zone 3'] = hr_zones_pre_convert['HR Zone 3'] / 3600
    hr_zones_only['HR Zone 4'] = hr_zones_pre_convert['HR Zone 4'] / 3600
    hr_zones_only['HR Zone 5'] = hr_zones_pre_convert['HR Zone 5'] / 3600
    plt.plot(hr_zones_only['HR Zone 1'], linestyle='-', color='#fedcda', label='HR Zone 1')
    plt.plot(hr_zones_only['HR Zone 2'], linestyle='-', color='#ff7f78', label='HR Zone 2')
    plt.plot(hr_zones_only['HR Zone 3'], linestyle='-', color='#ff2216', label='HR Zone 3')
    plt.plot(hr_zones_only['HR Zone 4'], linestyle='-', color='#b30900', label='HR Zone 4')
    plt.plot(hr_zones_only['HR Zone 5'], linestyle='-', color='#510400', label='HR Zone 5')
    plt.title('Time Spent in Heart Rate Zones Over Different Months')
    plt.xlabel('Month')
    plt.ylabel('Time Spent in HR Zones (in hours)')
    plt.legend()
    plt.savefig('visuals/trend_time_spent_in_hr_zones.png')
    plt.show()


if __name__ == '__main__':
    visualize()