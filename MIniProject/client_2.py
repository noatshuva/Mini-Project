import smtplib
from email.message import EmailMessage

# This client sends a mail with a file which contains a virus.

message = EmailMessage()
message['From'] = "noa@gmail.com"
message['To'] = "nitzan@gmail.com"
message['Subject'] = "Mini Project"

body = "Hi Nitzan,\n" \
       "I found this file in google and it has some interesting information about NetworkSecurity.\n"\
       "We can learn a lot from it, let me know when you done going through it and we'll talk about it.\n"\
       "Noa"
message.set_content(body)

with open("Files/infectedFile", 'rb') as file:
 message.add_attachment(file.read(), maintype="application", subtype="octet-stream",filename="Files/infectedFile")


with smtplib.SMTP('127.0.0.1', 30000) as server:
    server.sendmail("noa@gmail.com", "nitzan@gmail.com", message.as_string())
    server.quit()