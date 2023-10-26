import pandas as pd
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import joblib
from . import db
from .models import Predict
from datetime import datetime

views = Blueprint('views', __name__)


def predictor(data):
    df = pd.DataFrame(data, index=[0])
    load_model = joblib.load('./Models/classifier.joblib')
    result = load_model.predict(df)[0]
    return result
    

@views.route('/')
@login_required
def home():
    
    return render_template('home.html', user=current_user) 



@views.route('/predict', methods=['GET','POST'])
@login_required

def predict():
    if request.method == 'POST':
        sr = request.form.get('sr')
        rr = request.form.get('rr')
        t = request.form.get('temp')
        lm = request.form.get('lm')
        bo = request.form.get('bo')
        rem = request.form.get('rem')
        srh = request.form.get('sr.1')
        hr = request.form.get('hr')

        data = {
        "sr": sr,
        "rr": rr,
        "t": t,
        "lm": lm,
        "bo": bo,
        "rem": rem,
        "sr.1": srh,
        "hr": hr
        }
        result = predictor(data)
        if result == 0:
            stress_level = 0
        elif result == 1:
            stress_level= 1
        elif result == 2:
            stress_level = 2
        elif result==3:
            stress_level = 3
        else:
            stress_level = 4
        new_predict = Predict(stress=stress_level, user_id = current_user.id, sr=sr, rr=rr, t=t, lm=lm, bo=bo, rem = rem, srh=srh, hr=hr)
        db.session.add(new_predict)
        db.session.commit()
        
    return render_template('home.html', user=current_user, outcome=result)