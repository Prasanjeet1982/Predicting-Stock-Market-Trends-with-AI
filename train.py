import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from textblob import TextBlob

# Load and preprocess data
data = pd.read_csv('path_to_your_data.csv')

# Feature matrix X and target vector y
X = data[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_50', 'SMA_200', 'RSI', 'Sentiment']]
y = data['Target']

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train an XGBoost model
xgb_model = XGBClassifier(n_estimators=200, max_depth=5)
xgb_model.fit(X_train, y_train)
xgb_model.save_model('models/xgb_model.bin')

# Train an LSTM model
sequence_length = 30
X_lstm = []
y_lstm = []
for i in range(sequence_length, len(X_scaled)):
    X_lstm.append(X_scaled[i - sequence_length:i, :])
    y_lstm.append(y[i])
X_lstm, y_lstm = np.array(X_lstm), np.array(y_lstm)

model_lstm = Sequential()
model_lstm.add(LSTM(units=50, return_sequences=True, input_shape=(X_lstm.shape[1], X_lstm.shape[2])))
model_lstm.add(LSTM(units=50, return_sequences=False))
model_lstm.add(Dense(units=25))
model_lstm.add(Dense(units=1))
model_lstm.compile(optimizer='adam', loss='mean_squared_error')
model_lstm.fit(X_lstm, y_lstm, batch_size=64, epochs=50)
model_lstm.save('models/lstm_model.h5')
