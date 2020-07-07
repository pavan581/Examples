import smtplib
import ssl

port = 465
password = "pAvan@22052004"

context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
server.login("g.kumarpavan143@gmail.com",password)

sender_email = "g.kumarpavan143@gmail.com"
receiver_email = "sairam.g581@gmail.com"
message = "Hello world..."

server.sendmail(sender_email,receiver_email,message)
