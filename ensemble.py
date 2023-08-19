import numpy as np

def make_ensemble_prediction(xgb_model, lstm_model, scaled_features):
    xgb_prediction = xgb_model.predict(scaled_features)
    lstm_prediction = lstm_model.predict(np.array([scaled_features]))
    ensemble_prediction = xgb_prediction + lstm_prediction
    return ensemble_prediction
