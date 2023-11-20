import pickle

def predict(model_name, X_test):
    with open(f'models/{model_name}.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
        return loaded_model.predict(X_test)