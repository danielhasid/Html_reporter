import smtplib

gmail_user = 'dhasid1@gmail.com'
gmail_password = 'naqyeucrdivuvldk'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 25)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except smtplib.SMTPException as err:
    print(err)