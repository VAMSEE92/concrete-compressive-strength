from flask import Flask, jsonify, request,render_template
import pandas as pd
import numpy as np
import warnings
import pickle
import os
# os.chdir('E:\imp\Tasks\Concrete')
# Load Model
model=pickle.load(open('Finalmodel.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    print("home is called")
    return render_template('home.html')
@app.route('/api',methods=['POST'])
def predict():
    warnings.filterwarnings('ignore')
    #get data from post request
    data=request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data
    predict_request=[[data['cement'],data['slag'],data['ash'],data['water'],data['superplastic'],data['age']]]
    predict_request=np.array(predict_request)
    predict_request_df=pd.DataFrame(predict_request)
    # print(predict_request_df)
    prediction=model.predict(predict_request_df)
    # print(prediction)
    return jsonify(float(prediction))
@app.route('/predict',methods=['POST'])
def webApp():
    warnings.filterwarnings('ignore')
    # get data from post request
    predict_request=[[request.form.get("cement"),request.form.get('slag'),request.form.get('ash'),request.form.get('water'),request.form.get('superplastic'),request.form.get('coarseagg'),request.form.get('fineagg'),request.form.get('age')]]
    predict_request = np.array(predict_request)
    predict_request_df = pd.DataFrame(predict_request)
    # print(predict_request_df)
    prediction = model.predict(predict_request_df)
    # print(prediction)
    return render_template('home.html',prediction='Strength of concrete is {}'.format(prediction))



if __name__=='__main__':
    app.run(debug=True)

