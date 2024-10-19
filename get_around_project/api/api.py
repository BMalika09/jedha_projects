from fastapi import FastAPI
import joblib
import pandas as pd 
from typing import Literal, List, Union
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

app = FastAPI()

model = joblib.load('reg.pkl')
preprocessor = joblib.load('preprocessor.pkl')


class PredictionInput(BaseModel):
    car: str
    mileage: int
    engine_power: int
    fuel: str
    paint_color: str
    car_type: object
    private_parking_available: bool 
    has_gps : bool
    has_air_conditioning : bool
    automatic_car: bool
    has_getaround_connect : bool
    has_speed_regulator   :bool 
    winter_tires: bool  

@app.get("/", response_class=PlainTextResponse)
async def read_root():
    with open("README.md", "r") as f:
        content = f.read()
    return content

@app.post("/predict")
async def predict(input_data: PredictionInput):
    
    input_df = pd.DataFrame([input_data.dict()])
    preprocessed_data = preprocessor.transform(input_df)
    prediction = model.predict(preprocessed_data)
    return {"prediction": prediction[0]}


