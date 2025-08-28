#https://myaccount.google.com/apppasswords
#App Name is Gopi App
#password(9:25 AM):-scqd kgba wkds ayjs

import smtplib #Simple mail transfer protocal for sending mails
import os      # For File path and file existance check
import csv     #To read email addresses from a CSV file

#for creating multipart email messages
from email.mime.multipart import MIMEMultipart

#for adding plain text to email body
from email.mime.text import MIMEText


SMTP_SERVER="smtp.gmail.com"
SMTP_PORT= 587 #Port Used for TLS(encryption)
SENDER_EMAIL="gopiduriseti@gmail.com"
SENDER_PASSWORD="scqd kgba wkds ayjs"

def send_email(to_email,subject,body):
    try:
        msg=MIMEMultipart()
        msg["From"]=SENDER_EMAIL
        msg["To"]=to_email
    except:
        pass
