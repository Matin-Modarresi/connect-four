import smtplib , ssl,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

import urllib.request #same as urllib2

  
def email_sender(subject , body, filename , sender_email , receiver_email , password):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  
    
   
    message.attach(MIMEText(body, "plain"))  
    
   
    with open(filename, "rb") as attachment:

        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    

    encoders.encode_base64(part)
    
    part.add_header("Content-Disposition",f"attachment; filename= {filename}",)
    
    
    message.attach(part)
    text = message.as_string()
    
   
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def internet_check():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.request.URLError as err: 
        return False