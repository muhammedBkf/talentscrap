
# Python code to illustrate Sending mail with qr code as attachment
# from your Gmail account 
  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send(note) :  
    fromaddr = "mu7test@gmail.com"
    toaddr = "jm_boukerfa@esi.dz"
       
    # instance of MIMEMultipart
    msg = MIMEMultipart()
      
    # storing the senders email address  
    msg['From'] = fromaddr
      
    # storing the receivers email address 
    msg['To'] = toaddr
      
    # storing the subject 
    msg['Subject'] = "logm"
      
    # string to store the body of the mail
    body = "ta note est : " +str(note)
      
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
      
      
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
      
    # start TLS for security
    s.starttls()
      
    # Authentication
    s.login(fromaddr, "TEST@test@TEST")
      
    # Converts the Multipart msg into a string
    text = msg.as_string()
      
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
    


    
