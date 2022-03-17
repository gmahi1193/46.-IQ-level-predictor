# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:57:59 2022

@author: gmahi
"""

from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def iq_level():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        iq_lev = str(round(model.predict([[hours]])[0][0],2))

    return render_template('index.html', your_level = iq_lev)
    

if __name__ == '__main__':
    app.run(debug = True)
    


