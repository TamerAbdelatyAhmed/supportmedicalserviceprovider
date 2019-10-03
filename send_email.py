from email.mime.text import MIMEText
import smtplib

def send_email(Name, index, Email, Blood_pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes):
    from_email="myemail@gmail.com"
    from_password="mypassword"
    to_email=email

    subject="Patient Data Report"
    message="Hey there, your Medical Data Report is" + Print(Data(Name, index, Email, Blood_pressure, Blood_Glucose, Weight, Height, Body_Temp, Medications_History, Diseases_History, Notes))

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',465)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
