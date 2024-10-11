from email.message import EmailMessage
import smtplib
import ssl



email_sender= "urstarkjr@gmail.com"
email_pass= "mszw xmnx vmjq dpgw"
email_receiver="umeshkanna2004@gmail.com"

subject="Don't forget to manifest"

body="""
do your work man"""

em=EmailMessage()
em["From"]= email_sender
em["TO"]= email_receiver
em["subject"]= subject

em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as smtp:
    smtp.login(email_sender,email_pass)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

