from fastapi import FastAPI, Request, Form
from pydantic import BaseModel, Field
from src.predict import predict
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="web")


app = FastAPI(
    title="Customer Segmentation API",
    description="Predict customer segments using RFM values and KMeans.",
    version="1.0.0"
)


class RFM(BaseModel):
    recency: int = Field(..., ge=0)
    frequency: int = Field(..., ge=0)
    monetary: float = Field(..., ge=0)


class PredictionResponse(BaseModel):
    cluster: int
    name: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict-form", response_class=HTMLResponse)
def predict_form(request: Request, recency: int = Form(...), frequency: int = Form(...), monetary: float = Form(...)):
    rfm_values = [recency, frequency, monetary]
    cluster, name = predict(rfm_values)
    return templates.TemplateResponse("index.html", {"request": request, "cluster": cluster, "name": name})


@app.post("/predict", response_model=PredictionResponse)
def predict_customer_segment(rfm: RFM):
    rfm_values = [rfm.recency, rfm.frequency, rfm.monetary]
    cluster, name = predict(rfm_values)
    return PredictionResponse(cluster=cluster, name=name)


@app.get("/health")
def health_check():
    return {"status": "ok"}