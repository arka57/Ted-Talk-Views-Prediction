from flask import Flask,render_template,request
import pickle
import numpy as np

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
    days_old=int(request.form.get('days_old'))
    is_weekend=int(request.form.get('is_weekend'))
    alc=int(request.form.get('alc'))

    #prediction
    x=np.array([c,d,days_old,is_weekend,alc]).reshape(1,5)
    y=model1.transform(x)
    result=model.predict(y)
    result1=np.exp(result)  

    return render_template('index.html',result=result1)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)