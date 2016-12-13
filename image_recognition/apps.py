from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from werkzeug import secure_filename
import os
import pickle
import numpy as np

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# nn = pickle.load(open(os.path.join(APP_ROOT,
#                  'pkl_objects',
#                  'classifier.pkl'), 'rb'))

def classify(image):
    label = {0: 'safe', 1: 'unsafe'}
    X = image
    y = nn.predict(X)[0]
    proba = np.max(nn.predict_proba(X))
    return label[y], proba

def train(image, y):
    X = image
    nn.fit(X, [y], print_progress=True)


@app.route("/")
def index():
    return render_template("imageform.html")


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == 'POST':
        image = request.files['file']
        y = classify(image)
        target = os.path.join(APP_ROOT, 'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("file"):
            print(file)
            filename = file.filename
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)

        return render_template("results.html")
        
if __name__ == '__main__':
   app.run(debug = True)