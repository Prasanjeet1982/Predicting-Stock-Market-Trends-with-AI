from fastapi import FastAPI
from app.models.prediction import PredictionInput
from app.utils.preprocessing import get_scaled_features
from app.utils.model_loading import load_xgb_model, load_lstm_model
from app.models.ensemble import make_ensemble_prediction

app = FastAPI()

xgb_model = load_xgb_model('scripts/xgb_model.bin')
lstm_model = load_lstm_model('scripts/lstm_model.h5')

@app.post("/predict/")
def predict_price_movement(input_data: PredictionInput):
    scaled_features = get_scaled_features(input_data)
    ensemble_prediction = make_ensemble_prediction(xgb_model, lstm_model, scaled_features)
    return {"ensemble_prediction": int(ensemble_prediction[0])}
