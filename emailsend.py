__author__ = 'Suraj'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.encoders as Encoders
import os
import getpass

def send_email():
    msg = MIMEMultipart()
    
    #Personalize this Section
    me = "spachary@ncsu.edu"
    attach = "C:\\Users\\Suraj\\Documents\\Suraj Acharya.pdf"
    name = 'Suraj Acharya'
    subject = 'Random Subject'
    
    #Setup The connection to the Email App
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    email  = input("Email Address : ")
    pwd = getpass.getpass()
    s.login(email, pwd)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    while True:
        msg = MIMEMultipart()
        msg['From'] = name
        msg['Subject'] = subject
        msg.attach(part)
        myfile = open("email_body.txt" , "r")
        text = myfile.read()

        #Start the personalization
        
        to = input("Receiver Email : ")
        Name = input("Receiver Name : ")
        company_name = input("Company Name : ")
        text = text.replace("<<<company_name>>>" , company_name)
        text = text.replace("<<<Name>>>" , Name)

        msg.attach(MIMEText(text))

        #Confirm if the entered Information is correct
        print ("Confirm details : Email " + to + " Company Name : " + company_name + " Name is : " + Name)
        confirm = input("Hit 1 to confirm anything else to retry 0 to exit")
        if confirm == "1" :
            msg['To'] = to
            
            #Incase there is a connection broken due to timeout re create connection
            try:
                s.sendmail(me, to, msg.as_string())
            except:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.ehlo()
                s.starttls()
                s.login(email, pwd)
                s.sendmail(me, to, msg.as_string())
                
        #Exit the program
        elif confirm == "0":
            print("Exiting Module ")
            break
        else:
            continue



    s.quit()

send_email()



