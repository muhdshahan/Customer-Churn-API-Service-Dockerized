from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

model = joblib.load('models/model.joblib')

app = FastAPI()

class BankFeatures(BaseModel):
    Age: int
    Gender: str
    Balance: float
    EstimatedSalary: float
    NumOfProducts: int
    CreditScore: int
    IsActiveMember: int

@app.get('/')
def landing():
    return {"message": "Welcome to churn prediction model"}

@app.post('/predict')
def predict(val: BankFeatures):
    df = pd.DataFrame([val.dict()])  

    if val.Gender not in ['Male', 'Female']:
        raise HTTPException(status_code=400, detail='Invalid gender') 
    
    df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
    Prediction = model.predict(df)
    if Prediction == 1:
        return {"Prediction": 1,
                 "message": "The customer will Churn"}
    else:
        return {"Prediction": 0,
                 "message": "The customer does not Churn"}



