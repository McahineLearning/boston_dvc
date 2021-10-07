import re
import flask
import json
from flask import config
import numpy as np
import joblib
import pickle
import os
from flask import Flask, render_template, request
import yaml

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

app = Flask(__name__,template_folder=template_dir)


@app.route("/")
@app.route("/index")

def index():
	return flask.render_template('index.html')


@app.route("/predict",methods = ['POST'])
def make_predictions():

    config = read_params(config_path=params_path)
    model_dir = config['webapp_model_dir']

    with open(model_dir, 'rb') as f:
        reg = pickle.load(f)

    if request.method == 'POST':
        try:
            a = request.form.get('crim')
            c = request.form.get('indus')
            d = request.form.get('chas')
            e = request.form.get('nox')
            f = request.form.get('rm')
            g = request.form.get('age')
            h = request.form.get('dis')
            i = request.form.get('rad')
            j = request.form.get('tax')
            k = request.form.get('ptratio')
            l = request.form.get('b')
            m = request.form.get('lstat')
            
            X = np.array([[a,c,d,e,f,g,h,i,j,k,l,m]])
            pred = abs(reg.predict(X))
            pred = pred[0]
            pred = round(pred, 3)
            pred = str(pred)
            print(pred)
            return flask.render_template('predict.html', response = pred)

        except Exception as e:
            print(e)
        
        
if __name__ == '__main__':
   # importing models


    app.run(host='0.0.0.0', port=8001, debug=True)