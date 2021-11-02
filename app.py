#importing the libraries
import pickle
from flask import Flask,render_template,request

#global variable
lodedModel = pickle.load(open('Logistic Model.pkl','rb'))
app  = Flask(__name__)

#user-defined routes
@app.route("/")
def home():
    return render_template('heart.html')

@app.route("/prediction", methods=['POST'])
def prediction():
    cp = request.form['chest pain']
    restecg = request.form['restecg']
    thalach = request.form['max heart rate']
    slope = request.form['slope']

    prediction = lodedModel.predict([[cp,restecg,thalach,slope]])

    if prediction[0] == 0:
        prediction = "Not Heart Disease"
    else:
        prediction = "Heart Disease"

    return render_template('heart.html', output=prediction)     

#main function
if __name__=='__main__':
    app.run(debug=True)