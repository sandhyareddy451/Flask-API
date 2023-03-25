from flask import *

app= Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/student')
def student():
    return "returning student details"

#concatinating of two string
@app.route('/staff/<string>')
def staff(string):
    return "returning staff details of " + string

@app.route('/user/<name>')
def user(name):
    if name=="home":
        return redirect(url_for('home'))
    
    elif name=="student":
        return redirect(url_for('student'))
    
    elif name=="staff":
        return redirect(url_for('staff'))

if __name__=="__main__":
    app.run(debug=True)
