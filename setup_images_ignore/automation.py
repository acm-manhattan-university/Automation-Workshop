
import smtplib #for sending/sending with attahcment
import os#intearcting with files in os
#for sending with attachment 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
 
 #jj
 
#r
#receiving messages
import imaplib
import email
#server 
smtp_server = 'smtp.gmail.com'
#server port number
smtp_port = 587
#sender email address
smtp_username = os.getenv("SENDER") #
#sender email address password
smtp_password = os.getenv("IMAP_PASSWORD") 
#sender email address
from_email = os.getenv("SENDER") #
#receiver email address
to_email =  os.getenv("RECEIVER") #
#subject
subject = "yo contract or some shit?"
#email body
body = 'or maybe not'

#message = f'Subject: {subject}\n\n{body}'
#from_email,to_email,message

#for sending with attachment
msg = MIMEMultipart()
#sender email
msg['From'] = from_email
#receiver email
msg['To'] = to_email
#subject
msg['Subject'] = subject
#body
msg.attach(MIMEText(body))
#attachment being used
file_path = 'studentemploymentcontract.pdf'
#reading file, type(.docx,pdf) attaching message
with open(file_path,'rb') as f:
    attachment = MIMEApplication(f.read(),_subtype='pdf')
    attachment.add_header('Content-Disposition','attachment', filename='studentemploymentcontract.pdf')
    msg.attach(attachment)
    
    #actually sending message
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()#making sure email is secure
    #logging into email
    smtp.login(smtp_username,smtp_password)
    #actually sending email
    smtp.sendmail(from_email,to_email,msg.as_string())

 
 #rfg
 
#receiving

imap_server = 'imap.gmail.com'
imap_username = os.getenv("SENDER")
imap_password = os.getenv("IMAP_PASSWORD") 

#receivng subject and sender
with imaplib.IMAP4_SSL(imap_server) as imap:#logging into imap server
    imap.login(imap_username,imap_password)#loging into email
    imap.select('inbox') #inbox needed
    _, data = imap.search(None,'ALL') #searching for all emails
    latest_email_id = data[0].split()[-1]
    _, message_data = imap.fetch(latest_email_id,  '(RFC822)') # feteching recent email
    message = email.message_from_bytes(message_data[0][1])
    subject = message['Subject'] # recent subject
    sender = message['From']#recent message
    print(f'subject: {subject}') #subject
    print(f'sender: {sender}')#sender
 
   
   #maybe add(for actually reading emails. Had to use copilot since i couldnt find any documentation for this)
   #might or might not present this during workshop(people might get confused)
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            
            if "attachment" not in content_disposition:
                #plaintext
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    print(f'Message: {body}')
                    #html format 
                elif content_type == "text/html":
                    html_body = part.get_payload(decode=True).decode()
                    print(f'HTML Message: {html_body}')
    else:
        body = message.get_payload(decode=True).decode()
        print(f'Message: {body}')
        
        
