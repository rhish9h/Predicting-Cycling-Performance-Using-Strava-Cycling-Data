import pickle

def train_model(X_train, y_train, model, model_name):
    model.fit(X_train, y_train)
    with open('models/' + model_name + '.pkl', 'wb') as file:
        pickle.dump(model, file)