import numpy as np
from sklearn.preprocessing import MinMaxScaler

def get_scaled_features(input_data):
    features = [input_data.open, input_data.high, input_data.low, input_data.close,
                input_data.volume, input_data.sma_50, input_data.sma_200,
                input_data.rsi, input_data.sentiment]
    scaler = MinMaxScaler()
    scaler.fit(np.genfromtxt('scripts/scaler_data.csv', delimiter=','))
    scaled_features = scaler.transform([features])
    return scaled_features
