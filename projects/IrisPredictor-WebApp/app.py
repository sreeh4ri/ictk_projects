# Flask entry point
from flask import Flask, render_template, request
import pickle
import pandas as pd

# App
app = Flask(__name__)

# Load model
model_file = open('iris-model.pkl', 'rb')
model = pickle.load(model_file)
model_file.close()
# Define Routing


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    sl = round(float(request.values['sl']), 2)
    sw = round(float(request.values['sw']), 2)
    pl = round(float(request.values['pl']), 2)
    pw = round(float(request.values['pw']), 2)
    exp = pd.DataFrame({'SL':[sl], 'SW':[sw], 'PL':[pl], 'PW':[pw]})
    # Predict
    prediction = model.predict(exp).item()
    output = "Your Iris belongs to "+ get_iris_name(prediction)
    return render_template('result.html', prediction_text=output)

def get_iris_name(prediction):
    if 0 == prediction:
        return "Iris-setosa"
    elif 1 == prediction:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

if __name__ == '__main__':
    app.run(port=8000)
