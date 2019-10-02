from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
import smtplib

app=Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']="sqlite:////C:/datana/data.db"
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/data'
app.config['SQLALCHEMY_DATABASE_URI']="postgres://bhanumdxiqwwmb:c158369ee7766967b67a7fa36d4531aa8e0aa0fccf93042e24a8ad2e9a8ff320@ec2-107-21-201-238.compute-1.amazonaws.com:5432/d9bknqpmb4athe"
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    Name=db.Column(db.String(20), primary_key=True)
    index=db.Column(db.Integer(), unique=True)
    Email=db.Column(db.String(120), unique=True)
    Date=db.Column(db.Integer(), unique=True)
    Blood_Pressure=db.Column(db.String(120), unique=True)
    Blood_Glucose=db.Column(db.String(120), unique=True)
    Weight=db.Column(db.Integer(), unique=True)
    Height=db.Column(db.String(120), unique=True)
    Body_Temp=db.Column(db.Integer(), unique=True)
    Medications_History=db.Column(db.String(120), unique=True)
    Diseases_History=db.Column(db.String(120), unique=True)
    Notes=db.Column(db.String(120), unique=True)

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

Name = Data.Name
Email = Data.Email
Date = Data.Date
Blood_Pressure = Data.Blood_Pressure
Blood_Glucose = Data.Blood_Glucose
Weight = Data.Weight
Height = Data.Height
Body_Temp = Data.Body_Temp
Medications_History = Data.Medications_History
Diseases_History = Data.Diseases_History
Notes = Data.Notes
@app.route("/")
def index():
    return render_template("index.html")
    send_email(subject, msg)

@app.route("/success", methods=['POST'])
def success():
    Email=request.form["Email"]
    Height=request.form["Height"]
    print(Email, Height)
    data=Data(Name, index, Email, Date, Blood_Pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes)
    db.session.add(data)
    return render_template("success.html")
if __name__ == '__main__':
    app.debug=True
    app.run(port=5005)
