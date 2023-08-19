from pydantic import BaseModel

class PredictionInput(BaseModel):
    open: float
    high: float
    low: float
    close: float
    volume: float
    sma_50: float
    sma_200: float
    rsi: float
    sentiment: float
