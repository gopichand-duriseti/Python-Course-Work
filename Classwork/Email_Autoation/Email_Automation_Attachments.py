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

from email.mime.base import MIMEBase
from email import  encoders


SMTP_SERVER="smtp.gmail.com"
SMTP_PORT= 587 #Port Used for TLS(encryption)
SENDER_EMAIL="gopiduriseti@gmail.com"
SENDER_PASSWORD="scqd kgba wkds ayjs"

def send_email(to_email,subject,body,attachments):
    try:
        msg=MIMEMultipart()
        msg["From"]=SENDER_EMAIL
        msg["To"]=to_email
        msg["Subject"]=subject
        msg.attach(MIMEText(body,"plain"))
        print(msg,'************')
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path,"rb") as f:
                        mime_base=MIMEBase("application","octet-stream")
                        mime_base.set_payload(f.read()) #to read all content in binary format
                        encoders.encode_base64(mime_base)
                        mime_base.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(file_path)}"
                        )
                        msg.attach(mime_base)
                else:
                    print(f"File '{file_path}' not found.Skipping...")

        server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,to_email,msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}:{e}")
def send_bulk_email(csv_file,subject,body):
    try:
        csv_path=os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error:CSV file '{csv_file}' not found.")
            return
        with open(csv_path,newline="",encoding="utf-8") as file:
            reader=csv.reader(file)
            next(reader,None)
            print(reader,"reader")
            for row in reader:
                if row:
                    email=row[0]
                    send_email(email,subject,body)
    except Exception as e:
        print(f'Error reading file:{e}')