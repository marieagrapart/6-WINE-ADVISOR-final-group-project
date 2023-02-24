import json
import mlflow 
import uvicorn

import pandas as pd 
import tensorflow
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile

import os
print(os.environ)
target = open("target.json")
target = json.load(target)

description = """
Welcome to  API.  Try it out 

## Introduction Endpoints

"""
tags_metadata = [
    {
        "name": "Introduction Endpoints",
        "description": "Simple endpoints to try out!",
    },
    {
        "name": "Machine Learning",
        "description": "Prediction vin."
    }
]

app = FastAPI(
    title="On boit quoi avec ça ?",
    description=description,
    version="0.1",
    contact={
        "name": "On boit quoi avec ça ?",
        
    },
    openapi_tags=tags_metadata
)
class PredictionFeatures(BaseModel):
    plat: str = "osso buco"
    
@app.get("/", tags=["Introduction Endpoints"])
async def index():
    """
    Renvoie simplement un message de bienvenue !
    """
    message = "Bonjour! Ce `/` est le point de terminaison le plus simple et par défaut. Si vous voulez en savoir plus, consultez la documentation de l'API sur `/docs`"
    return message

@app.post("/predict", tags=["Machine Learning"])
async def predict(predictionFeatures: PredictionFeatures):
    """
    Prediction du vin 
    """
    plat = pd.DataFrame(dict(predictionFeatures), index=[0])
                         
    logged_model = 'runs:/9a61dc4926804f6e93d7013c8b5efcba/models.joblib'

    logged_model = mlflow.pyfunc.load_model(logged_model)

    prediction = logged_model.predict(plat)

    valeur = prediction.values.tolist()[0]

    max_value = max(valeur)

    max_index = valeur.index(max_value)
    
    response = target[str(max_index)]

    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)

