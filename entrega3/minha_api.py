# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("minha_api")

# Define input and output Pydantic models
class Input(BaseModel):
    Age: int
    Gender_Female: int
    Gender_Male: int

class Output(BaseModel):
    prediction: float

# Define predict function
@app.post("/predict", response_model=Output)
def predict(data: Input):
    data_dict = data.dict()
    data_df = pd.DataFrame([data_dict])
    predictions = predict_model(model, data=data_df)
    print(predictions.columns) #Enxegar as colunas do dataframe de saída
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
