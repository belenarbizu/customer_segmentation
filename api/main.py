from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.predict import predict


app = FastAPI(
    title="Customer Segmentation API",
    description="Predict customer segments using RFM values and KMeans.",
    version="1.0.0"
)


class RFM(BaseModel):
    recency: int = Field(..., ge=0)
    frequency: int = Field(..., ge=0)
    monetary_value: float = Field(..., ge=0)


class PredictionResponse(BaseModel):
    cluster: int
    name: str


@app.post("/predict", response_model=PredictionResponse)
def predict_customer_segment(rfm: RFM):
    rfm_values = [rfm.recency, rfm.frequency, rfm.monetary_value]
    cluster, name = predict(rfm_values)
    return PredictionResponse(cluster=cluster, name=name)


@app.get("/health")
def health_check():
    return {"status": "ok"}