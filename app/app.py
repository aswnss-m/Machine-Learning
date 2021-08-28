from flask import Flask,render_template,request,redirect
import pickle
import pandas as pd
import numpy as np

with open("Laura/Assets/Model/locations.txt", "r") as f:
    locations = f.read()
    locations = locations.strip()[1:len(locations)-1]
    locations = locations.split(',')
    location_data = [i.strip() for i in locations]
    #These datapoints have "'" as a data among them so , and striping the "'" in each name
    locations = [i[1:len(i)-1] for i in location_data if i != "'"]
ans = 0
def predict_price(location,sqft,bath,bhk):
    X = pd.read_csv("Laura/Assets/Model/Database.csv",sep=',')
    pickle_in = open("Laura/Assets/Model/Laura_Best_Model.pickle","rb")
    Laura = pickle.load(pickle_in)
    try:
        loc_index = np.where(X.columns==location)[0][0]
    except:
        loc_index = 0
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>0:
        x[loc_index] = 1
        
    ans = Laura.predict([x])[0]
    return ans


app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        return redirect('/'+name)
    else:
        return render_template('index.html')

@app.route('/<string:name>',methods=['GET','POST'])
def predict(name):
    if request.method == 'POST':
        Location = request.form['location']
        print(Location)
        Sqft = float(request.form['sqft'])
        bed = int(request.form['bed']) 
        bath = int(request.form['bath'])
        predicted_price = predict_price(location=Location, sqft=Sqft, bath=bath, bhk=bed)
        return redirect('/'+name+'/results='+ str(predicted_price))
    return render_template('predict.html',name=name,locations = locations)

@app.route('/<string:name>/results=<string:ans>')
def show_result(name,ans):
    return render_template('result.html',ans = float(ans))

if __name__=='__main__':
    app.run(debug=True)