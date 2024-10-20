import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'test23889922@gmail.com'
smtp_password = 'somepassword'

from_email = 'test23889922@gmail.com'
to_email =  'philippeaustephen@gmail.com'
subject = "yo contract?"
body = 'or maybe not'

#message = f'Subject: {subject}\n\n{body}'
#from_email,to_email,message

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body))

file_path = 'studentemploymentcontract.pdf'
with open(file_path,'rb') as f:
    attachment = MIMEApplication(f.read(),_subtype='pdf')
    attachment.add_header('Content-Disposition','attachment', filename='studentemploymentcontract')
    msg.attach(attachment)
    
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username,smtp_password)
    smtp.sendmail(from_email,to_email,msg.as_string())
