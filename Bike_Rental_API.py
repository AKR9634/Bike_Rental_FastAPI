from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field, computed_field, model_validator, field_validator
from typing import Literal, Annotated, Optional
import pandas as pd
from fastapi.responses import JSONResponse
import joblib

def load_data():
    data = pd.read_csv("Jupyter Notebook/Data.csv")
    return data

def load_model():
    model = joblib.load("Model/best_bike_model.pkl")
    return model

app = FastAPI()

class Bike_Input(BaseModel):

    season : Annotated[Literal[1, 2, 3, 4], Field(..., description= "Name of the Season!!!")]
    yr : Annotated[Literal[0, 1], Field(..., description= " 0 is for 2011 and 1 is for 2012!!!")]
    mnth : Annotated[int, Field(..., description= "Month of the year!!!")]
    holiday : Annotated[Literal[0, 1], Field(..., description="Holiday or not!!!")]
    weekday : Annotated[Literal[0, 1, 2, 3, 4, 5, 6], Field(..., description="Day of the week!!!")]
    workingday : Annotated[Literal[0, 1], Field(..., description="If the day is neither weekend nor holiday then 1, otherwiese 0!!!")]
    weathersit : Annotated[Literal[0, 1, 2], Field(..., description="Type of the weather!!!")]
    temp : Annotated[float, Field(..., description="Normalized Temperature in Celsius!!!")]
    atemp : Annotated[float, Field(..., description="Normalized feeling Temperature in Celsius!!!")]
    hum : Annotated[float, Field(..., description="Normalized Humidity!!!")]
    windspeed : Annotated[float, Field(..., description="Normalized wind speed!!!")]
    year : Annotated[Literal[2011, 2012], Field(..., description="Year!!!")]
    month : Annotated[int, Field(..., description="Month!!!")]
    day : Annotated[int, Field(..., description="Day!!!")]
    dayofweek : Annotated[int, Field(..., description="Day of the week!!!")]

class predicted_output(BaseModel):

    bike_count : Annotated[int, Field(..., description="The Bike count predicted!!!")]


@app.get("/")
def home():
    return {"message":"Bike Rental Predictor!!!"}

@app.get("/about")
def about():
    return {"message":"This page predicts the count of bike rents on the basis of the various inputs such as weekend, season, temperature, humidity and other factors...."}

@app.get("/view")
def view(sort_by: Optional[str] = Query(None, description="Field to sort the data!!!")):
    data = load_data()

    df = data.copy()

    if sort_by: 
        df.sort_values(by=sort_by, inplace=True)

    return df.to_dict(orient="records")

@app.post("/predict", response_model= predicted_output)
def predict_bike_counts(data:Bike_Input):

    input = {
        'season' : data.season,
        'yr' : data.yr,
        'mnth' : data.mnth,
        'holiday' : data.holiday,
        'weekday' : data.weekday,
        'workingday' : data.workingday,
        'weathersit' : data.weathersit,
        'temp' : data.temp,
        'atemp' : data.atemp,
        'hum' : data.hum,
        'windspeed' : data.windspeed,
        'year' : data.year,
        'month' : data.month,
        'day' : data.day,
        'dayofweek' : data.dayofweek
    }

    try:
        model = load_model()
        
        input_df = pd.DataFrame([input])

        prediction = model.predict(input_df)[0]

        prediction_dict = {}
        prediction_dict["Bike_Count"] = round(prediction)

        return JSONResponse(status_code=200, content={"Response" : prediction_dict})
    
    except Exception as e:
        return JSONResponse(status_code=500, content = str(e))