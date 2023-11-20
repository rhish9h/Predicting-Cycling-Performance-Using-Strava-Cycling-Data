import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import wf_ml_training
import wf_ml_prediction
from sklearn.metrics import mean_squared_error, r2_score

def evaluate():
    zones_ftp_power_agg = pd.read_csv('data_processed/zones_ftp_power_agg.csv')
    X_train, X_test, y_train, y_test = train_test_split(zones_ftp_power_agg.iloc[:, :-1], zones_ftp_power_agg.iloc[:, -1], test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    wf_ml_training.train_model(X_train_scaled, y_train, LinearRegression(), 'linear_regression_power_small')
    y_pred = wf_ml_prediction.predict('linear_regression_power_small', X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print evaluation metrics
    print(f'Mean Squared Error: {mse}')
    print(f'R-squared: {r2}')


if __name__ == '__main__':
    evaluate()