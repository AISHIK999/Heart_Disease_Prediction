from flask import Flask, render_template, request
import pandas as pd
from tensorflow.python.keras.models import load_model
import numpy as np


app = Flask(__name__)
model = load_model('model/heart_model.h5')


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    data = pd.read_csv(file)
    pred = model.predict(data)
    y_pred = np.round(pred).astype(int)

    data['Result'] = y_pred

    return render_template('result.html', data=data.to_html())


if __name__ == '__main__':
    app.run(debug=True)