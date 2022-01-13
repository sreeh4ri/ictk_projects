# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 22:05:10 2022
@author: sreeh4ri
"""
# Flask entry point
from flask import Flask, render_template, request
import pickle
import numpy as np

# App
app = Flask(__name__)

# Load model
model_file = open('model.pkl', 'rb')
model = pickle.load(model_file)
model_file.close()
# Define Routing


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
# url for predict, when ever /predict is loaded it opens predict form
def predict():
    exp = float(request.values['experience'])
    exp = np.reshape(exp, (-1, 1))
    prediction = model.predict(exp).item()
    prediction = round(prediction, 2)
    output = "Congrats!!... You are eligible for a salary of Rs.{}".format(
        prediction)
    return render_template('result.html', prediction_text=output)


if __name__ == '__main__':
    app.run(port=8000)
