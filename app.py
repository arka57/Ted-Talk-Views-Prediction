from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

model=pickle.load(open('model.pkl','rb'))
model1=pickle.load(open('model1.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_ted_talk_views():
    c=float(request.form.get('comments'))
    d=float(request.form.get('duration'))
    p_date=request.form.get('p_date')
    r_date=request.form.get('r_date')

    recorded_date=pd.to_datetime(r_date)
    published_date=pd.to_datetime(p_date)
    days_old=(published_date-recorded_date).days
    is_weekend=published_date.dayofweek
    #converting weekend-1 and otherwise-0
    if is_weekend >=5:
        is_weekend=1
    else:
        is_weekend=0    
    alc=int(request.form.get('alc'))

    #prediction
    x=np.array([c,d,days_old,is_weekend,alc]).reshape(1,5)
    y=model1.transform(x)
    result=model.predict(y)
    result1=np.exp(result) 

    return render_template('index.html',result=result1)


if __name__ == '__main__':
    app.run(debug=True)