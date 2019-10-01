from email.mime.text import MIMEText
import smtplib

def send_email(Email, Weight, Height, Blood_pressure, Blood_Glucose, Body_Temp):
    from_email="myemail@gmail.com"
    from_password="mypassword"
    to_email=email

    subject="Patient Data Report"
    message="Hey there, your Medical Data Report is" + Print(Data(Email, Weight, Height, Blood_pressure, Blood_Glucose, Body_Temp))

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',465)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
