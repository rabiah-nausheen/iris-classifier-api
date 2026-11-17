# model_training.py

import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
import pickle 
import os 


#Load dataset
data = load_iris(as_frame = True)
df = data['data']
target = data['target']

#Selecting a few features
selected_features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X = df[selected_features]
y = target 

#Train-test split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

#Train the Regressor 
model = SVC()
model.fit(X_train, y_train)

#Create a model folder to save the trained model 
os.makedirs('model', exist_ok=True)

#Save the trained model using pickle 
with open('model\svm_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved")