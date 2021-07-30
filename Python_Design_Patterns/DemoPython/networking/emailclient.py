import smtplib
from email.mime.text import MIMEText

body = ' This is a test email, How are you ?'
msg = MIMEText(body)
msg['From'] = 'shankkalra@gmail.com'
msg['To'] = 'er.shankkalra@gmail.com'
msg['Subject'] = 'Hello'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('shankkalra@gmail.com','**')
server.send_message(msg)

print('Mail Sent')

server.quit()