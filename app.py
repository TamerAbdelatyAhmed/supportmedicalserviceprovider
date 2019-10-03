#Import dependencies
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
#Create instance of Flask App
app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = True
#Connect to the Database
app.config['SQLALCHEMY_DATABASE_URI']="postgres://ypenmacgwpxmfm:0e3d4ca190f9742e0f25a56c2a51d9075e3cf28bb3e0c2e44128f52f180bb69a@ec2-107-20-167-241.compute-1.amazonaws.com:5432/ddq8054gd9prrv"
db=SQLAlchemy(app)
 
#create a table
class Data(db.Model):
    __tablename__="data"
    index=db.Column(db.Integer, primary_key=True)
    Name=db.Column(db.String) 
    Email=db.Column(db.String) 
    Blood_Pressure=db.Column(db.String)
    Blood_Glucose=db.Column(db.String)
    Weight=db.Column(db.Integer)
    Height=db.Column(db.String)
    Body_Temp=db.Column(db.Integer)
    Medications_History=db.Column(db.String)
    Diseases_History=db.Column(db.String)
    Notes=db.Column(db.String)

    def __init__(self, index, Name,  Email, Blood_Pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes):
        self.index=index
        self.Name = Name
        self.Email=Email
        self.Blood_Pressure=Blood_Pressure
        self.Blood_Glucose=Blood_Glucose
        self.Weight=Weight
        self.Height=Height
        self.Body_Temp=Body_Temp
        self.Medications_History=Medications_History
        self.Diseases_History=Diseases_History
        self.Notes=Notes

db.create_all()


#Define Route and Contant of that page
@app.route("/")
def index():
    return render_template("index.html")

#Define 2nd Route and Content
@app.route("/success", methods=['POST'])
def success():
    if(request.method == 'POST'):
        index=request.form["index"]
        Name=request.form["Name"]
        Email=request.form["Email"]
        Blood_Pressure=request.form["Blood_Pressure"]
        Blood_Glucose=request.form["Blood_Glucose"]
        Weight=request.form["Weight"]
        Height=request.form["Height"]
        Body_Temp=request.form["Body_Temp"]
        Medications_History=request.form["Medications_History"]
        Diseases_History=request.form["Diseases_History"]
        Notes = request.form["Notes"]  
        data=Data(index, Name, Email, Blood_Pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")
    return render_template('index.html', text="Seems like we got something from that email once!")

#Running and Controlling the script
if __name__ == '__main__':
    app.debug=True
    app.run(port=5004)
    
