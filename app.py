import pickle
import pandas as pd
from flask import Flask, render_template, request

# Create an object of the class Flask

app = Flask(__name__)
model = pickle.load(open('model/clf.pkl','rb'))



# url/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
# Make a prediction
def predict():
    data = {
        "sr": request.form.get('sr'),
        "rr": request.form.get('rr'),
        "t": request.form.get('t'),
        "lm": request.form.get('lm'),
        "bo": request.form.get('bo'),
        "rem": request.form.get('rem'),
        "sr.1": request.form.get('sr.1'),
        "hr": request.form.get('hr')
    }
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)[0]
           
    return render_template("index.html", prediction = prediction)

if __name__ == '__main__':
    app.run(debug=True)