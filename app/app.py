from flask import Flask,render_template,request,redirect

with open("Laura/Assets/Model/locations.txt", "r") as f:
    locations = f.read()
    locations = locations.strip()[1:len(locations)-1]
    locations = locations.split(',')
    location_data = [i.strip() for i in locations]
    #These datapoints have "'" as a data among them so , and striping the "'" in each name
    locations = [i[1:len(i)-1] for i in location_data if i != "'"]



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
        Sqft = float(request.form['sqft'])
        N_BHK = request.data
        print(N_BHK)
    return render_template('predict.html',name=name,locations = locations)
if __name__=='__main__':
    app.run(debug=True)