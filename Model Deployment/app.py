import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle
import pandas as pd

featdf=pd.read_csv('Model Deployment/features.csv')
feat=[]
for i in featdf.iterrows():
    f=[]
    for j in i:
        f.append(j)
    feat.append(f)

app= Flask(__name__)
model = pickle.load(open("Model Deployment\model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods =['POST'])
def predict():
    #float_features = [float(x) for x in request.form.values()]
    features= [np.array(feat[0])]
    prediction = model.prediction(features)

    return render_template("index.html",prediction_text = "Retirement years is {}".format(prediction))

if __name__ =="__main__":
    app.run(debug=True)
 