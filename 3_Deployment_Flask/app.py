import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import os

# Create flask app
app = Flask(__name__)

# Load pickle model
#model = pickle.load(open('rfc_model.pkl', 'rb'))
model = joblib.load('rfc_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)


    if prediction == 0:
        prediction = str('Not Fraud')
    else:
        prediction = str('Fraud')

    #output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Provider is probably: {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host=os.getenv('IP', '0.0.0.0'),
     #       port=int(os.getenv('PORT', 4444)))