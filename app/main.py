# app/main.py

from fastapi import FastAPI 
from pydantic import BaseModel, Field
import pickle 
import os 

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

# Define the input schema using Pydantic 
class InputData(BaseModel):
    sepal_length: float = Field(..., alias="sepal length (cm)")
    sepal_width: float = Field(..., alias="sepal width (cm)")
    petal_length: float = Field(..., alias="petal length (cm)")
    petal_width: float = Field(..., alias="petal width (cm)")

    model_config = {"populate_by_name": True}

# Initialize the FastAPI app 
app = FastAPI(title = "Iris Species Prediction API")

#Load the model 
model_path = os.path.join("model", "svm_model.pkl")
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: InputData):

    #Prepare the data for prediction 
    input_features = [[data.sepal_length, data.sepal_width,
                       data.petal_length, data.petal_width]]

    #Make predictions using the loaded model 
    prediction = int(model.predict(input_features)[0])

    #Return the prediction result 
    return {"predicted_iris_species": CLASS_NAMES[prediction]}