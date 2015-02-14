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
    me = "spachary@ncsu.edu"

    attach = "C:\\Users\\Suraj\\Documents\\Suraj Acharya.pdf"
    msg['From'] = 'Suraj Acharya'
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    pwd = getpass.getpass()
    email  = input("Email Address")
    s.login(email, pwd)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    while True:
        msg = MIMEMultipart()
        msg['From'] = 'Suraj Acharya'
        msg['Subject'] = 'Random Subject'
        msg.attach(part)
        myfile = open("email_body.txt" , "r")
        text = myfile.read()

        to = input("Receiver Email: ")
        Name = input("Receiver Name : ")
        company_name = input("Company Name : ")
        text = text.replace("<<<company_name>>>" , company_name)
        text = text.replace("<<<Name>>>" , Name)

        msg.attach(MIMEText(text))

        print ("Confirm details : Email " + to + " Company Name : " + company_name + " Name is : " + Name)
        confirm = input("Hit 1 to confirm anything else to retry 0 to exit")
        if confirm == "1" :
            msg['To'] = to
            s.sendmail(me, to, msg.as_string())
        elif confirm == "0":
            print("Exiting Module ")
            break
        else:
            continue



    s.quit()

send_email()



