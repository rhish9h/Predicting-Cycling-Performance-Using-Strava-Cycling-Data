import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
import wf_ml_training
import wf_ml_prediction
from sklearn.metrics import mean_squared_error, r2_score

def get_errors(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

def split_without_transform(filepath):
    zones_ftp_power_agg = pd.read_csv(f'data_processed/{filepath}.csv')
    X_train, X_test, y_train, y_test = train_test_split(zones_ftp_power_agg.iloc[:, :-1], zones_ftp_power_agg.iloc[:, -1], test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def split_and_transform(filepath):
    zones_ftp_power_agg = pd.read_csv(f'data_processed/{filepath}.csv')
    X_train, X_test, y_train, y_test = train_test_split(zones_ftp_power_agg.iloc[:, :-1], zones_ftp_power_agg.iloc[:, -1], test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, y_train, y_test

def train_predict_get_errors(filepath, ml_model, model_name):
    X_train_scaled, X_test_scaled, y_train, y_test = split_and_transform(filepath)
    wf_ml_training.train_model(X_train_scaled, y_train, ml_model, filepath + '_' + model_name)
    y_pred = wf_ml_prediction.predict(filepath + '_' + model_name, X_test_scaled)
    mse, r2 = get_errors(y_test, y_pred)
    return mse, r2

def write_first_to_summary_file(summary, summary_filepath):
    with open(summary_filepath, 'w') as file:
        file.write('First model:\n\n')
        print('First model:\n')
        file.write(f'{"Dataset":40} {"Method":20} {"MSE":>20} {"R2":>20}\n')
        print(f'{"Dataset":40} {"Method":20} {"MSE":>20} {"R2":>20}')
        row=summary.iloc[0]
        file.write(f"{row.loc['Dataset']:40} {row.loc['Method']:20} {row.loc['MSE']:20.10f} {row.loc['R2']:20.10f}\n")
        print(f"{row.loc['Dataset']:40} {row.loc['Method']:20} {row.loc['MSE']:20.10f} {row.loc['R2']:20.10f}")

def write_summary_to_file(summary, summary_filepath):
    with open(summary_filepath, '+a') as file:
        file.write('\nAll models including alternative models:\n\n')
        print('\nAll models including alternative models:\n')
        file.write(f'{"Dataset":40} {"Method":20} {"MSE":>20} {"R2":>20}\n')
        print(f'{"Dataset":40} {"Method":20} {"MSE":>20} {"R2":>20}')

        for _, row in summary.iterrows():
            file.write(f"{row.loc['Dataset']:40} {row.loc['Method']:20} {row.loc['MSE']:20.10f} {row.loc['R2']:20.10f}\n")
            print(f"{row.loc['Dataset']:40} {row.loc['Method']:20} {row.loc['MSE']:20.10f} {row.loc['R2']:20.10f}")

def predict_to_understand(filepath, model_name, ml_model):
    X_train_scaled, X_test_scaled, y_train, y_test = split_and_transform(filepath)
    wf_ml_training.train_model(X_train_scaled, y_train, ml_model, filepath + '_' + model_name)
    y_pred = wf_ml_prediction.predict(filepath + '_' + model_name, X_test_scaled)
    
    _, X_test, _, _ = split_without_transform(filepath)
    print(f'Using model {model_name} on dataset {filepath}.\n')

    print(f'input variables: {X_test.iloc[0]}')
    print(f'predicted FTP: {y_pred[0]}')
    print(f'actual FTP: {y_test.iloc[0]}\n')

    print(f'input variables: {X_test.iloc[5]}')
    print(f'predicted FTP: {y_pred[5]}')
    print(f'actual FTP: {y_test.iloc[5]}\n')

def variable_change_experiment(X_test, scaler, filepath, model_name, variableA, variableB=None, inverse=False):
    X_test_default = X_test.iloc[5:6]

    if variableA:
        init_variableA = X_test_default.at[X_test_default.index[0], variableA]
        print('init variable A', init_variableA)

    if variableB:
        init_variableB = X_test_default.at[X_test_default.index[0], variableB]
        print('init variable B', init_variableB)

    for i in range(5):
        X_test_cur = X_test.iloc[5:6].copy()
        if variableA:
            if inverse:
                new_value_A = init_variableA - (i+1) * 100
            else:
                new_value_A = init_variableA + (i+1) * 100
            print('new variable A', new_value_A)
            X_test_cur.at[X_test_cur.index[0], variableA] = new_value_A
        if variableB:
            new_value_B = init_variableB + (i+1) * 100
            print('new variable B', new_value_B)
            X_test_cur.at[X_test_cur.index[0], variableB] = new_value_B
        X_test_cur_scaled = scaler.transform(X_test_cur)
        y_pred_cur = wf_ml_prediction.predict(filepath + '_' + model_name, X_test_cur_scaled)
        print(f'Changed ', y_pred_cur)

def feature_importance_experiment(filepath, model_name, ml_model):
    zones_ftp_power_agg = pd.read_csv(f'data_processed/{filepath}.csv')
    X_train, X_test, y_train, y_test = train_test_split(zones_ftp_power_agg.iloc[:, :-1], zones_ftp_power_agg.iloc[:, -1], test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    wf_ml_training.train_model(X_train_scaled, y_train, ml_model, filepath + '_' + model_name)
    y_pred = wf_ml_prediction.predict(filepath + '_' + model_name, X_test_scaled)
    
    _, X_test, _, _ = split_without_transform(filepath)
    print(f'Using model {model_name} on dataset {filepath}.\n')

    print(f'input variables: {X_test.iloc[5]}')
    print(f'predicted FTP: {y_pred[5]}')
    print(f'actual FTP: {y_test.iloc[5]}\n')

    print('Increase variable A: average_heartrate\n')
    variable_change_experiment(X_test, scaler, filepath, model_name, 'average_heartrate')

    print('\nIncrease variable B: Power Zone 7\n')
    variable_change_experiment(X_test, scaler, filepath, model_name, None, 'Power Zone 7')

    print('\nIncrease both variable A and B: average_heartrate and Power Zone 7\n')
    variable_change_experiment(X_test, scaler, filepath, model_name, 'average_heartrate', 'Power Zone 7')

    print('\nDecrease variable A and increase B: average_heartrate and Power Zone 7\n')
    variable_change_experiment(X_test, scaler, filepath, model_name, 'average_heartrate', 'Power Zone 7', inverse=True)

def evaluate():
    summary_columns = ['Dataset', 'Method', 'MSE', 'R2']
    summary = pd.DataFrame(columns=summary_columns)

    datasets = ['zones_ftp_power_agg', 'zones_ftp_hr_agg', 'zones_ftp_power_hr_agg',
                'zones_ftp_power_agg_augmented', 'zones_ftp_hr_agg_augmented', 'zones_ftp_power_hr_agg_augmented']
    models = [('Linear Regression', LinearRegression()), ('Ridge', Ridge()), ('Lasso', Lasso())]

    for model_name, model in models:
        for dataset in datasets:
            mse, r2 = train_predict_get_errors(dataset, model, model_name)
            summary.loc[len(summary)] = [dataset, model_name, mse, r2]

    print('-----------------------------Summary-----------------------------')

    summary_filepath = 'evaluation/summary.txt'
    write_first_to_summary_file(summary, summary_filepath)
    write_summary_to_file(summary, summary_filepath)

    print('\n-----------------------Experiment 1----------------------------')
    predict_to_understand('zones_ftp_power_hr_agg', 'Lasso', Lasso())

    print('\n-----------------------Experiment 2----------------------------')
    feature_importance_experiment('zones_ftp_power_hr_agg', 'Lasso', Lasso())

if __name__ == '__main__':
    evaluate()