#Import dependencies
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#Create instance of Flask App
app = Flask(__name__)

#Connect to the Database
app.config['SQLALCHEMY_DATABASE_URI']="postgres://ypenmacgwpxmfm:0e3d4ca190f9742e0f25a56c2a51d9075e3cf28bb3e0c2e44128f52f180bb69a@ec2-107-20-167-241.compute-1.amazonaws.com:5432/ddq8054gd9prrv"
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    Name=db.Column(db.String, primary_key=True)
    index=db.Column(db.Integer)
    Email=db.Column(db.String) 
    Date=db.Column(db.Integer)
    Blood_Pressure=db.Column(db.String)
    Blood_Glucose=db.Column(db.String)
    Weight=db.Column(db.Integer)
    Height=db.Column(db.String)
    Body_Temp=db.Column(db.Integer)
    Medications_History=db.Column(db.String)
    Diseases_History=db.Column(db.String)
    Notes=db.Column(db.String)

    def __init__(self, Name, index, Email, Date, Blood_Pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes):
        self.Name = Name
        self.index=index
        self.Email=Email
        self.Date=Date
        self.Blood_Pressure=Blood_Pressure
        self.Blood_Glucose=Blood_Glucose
        self.Weight=Weight
        self.Height=Height
        self.Body_Temp=Body_Temp
        self.Medications_History=Medications_History
        self.Diseases_History=Diseases_History
        self.Notes=Notes


#Define Route and Contant of that page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if(request.method == 'POST'):
        Name_=request.form["Name"]
        index_=request.form["index"]
        Email_=request.form["Email"]
        Date_=request.form["Date"]
        Blood_Pressure_=request.form["Blood_Pressure"]
        Blood_Glucose_=request.form["Blood_Glucose"]
        Weight_=request.form["Weight"]
        Height_=request.form["Height"]
        Body_Temp_=request.form["Body_Temp"]
        Medications_History_=request.form["Medications_History"]
        Diseases_History_=request.form["Diseases_History"]
        Notes_=request.form["Notes"]
        data=Data(Name_, index_, Email_, Date_, Blood_Pressure_, Blood_Glucose_, Weight_, Height_, Body_Temp_, Medications_History_, Diseases_History_, Notes_)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")
if __name__ == '__main__':
    app.debug=True
    
