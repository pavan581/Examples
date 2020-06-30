import smtplib
import ssl

port = 465
password = "myPassword"

context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
server.login("myMail",password)

sender_email = "myMail"
receiver_email = "mail"
message = "Hello world..."

server.sendmail(sender_email,receiver_email,message)
