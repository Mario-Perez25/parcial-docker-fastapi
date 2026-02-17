from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="API ML Parcial")

model = joblib.load("modelo.pkl")

class InputData(BaseModel):
    edad: int
    ingresos: float

@app.get("/")
def test_endpoint():
    return {"mensaje": "API funcionando correctamente"}

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([[data.edad, data.ingresos]])
    return {"prediccion": int(prediction[0])}

