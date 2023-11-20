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

def evaluate():
    summary_columns = ['Dataset', 'Method', 'MSE', 'R2']
    summary = pd.DataFrame(columns=summary_columns)
    datasets = ['zones_ftp_power_agg', 'zones_ftp_hr_agg', 'zones_ftp_power_hr_agg',
                'zones_ftp_power_agg_augmented', 'zones_ftp_hr_agg_augmented', 'zones_ftp_power_hr_agg_augmented']
    models = [('Linear Regression', LinearRegression()), ('Ridge', Ridge()), ('Lasso', Lasso())]

    for dataset in datasets:
        for model_name, model in models:
            mse, r2 = train_predict_get_errors(dataset, model, model_name)
            summary.loc[len(summary)] = [dataset, model_name, mse, r2]

    print('-----------------------------Summary-----------------------------')
    print(summary)
    

if __name__ == '__main__':
    evaluate()