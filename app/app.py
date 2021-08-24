from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        return redirect('/'+name)
    else:
        return render_template('index.html')

@app.route('/<string:name>')
def predict(name):
    return "Hello " + name
if __name__=='__main__':
    app.run(debug=True)