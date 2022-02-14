import smtplib
from email.message import EmailMessage

# This client sends a mail with a photo with a suspicious name

message = EmailMessage()
message['From'] = "noa@gmail.com"
message['To'] = "nitzan@gmail.com"
message['Subject'] = "Mini Project"

body = "Hi Nitzan\n" \
       "You have to see this photo I found,\n" \
       "I think it can really helps us complete our project."
message.set_content(body)

with open("Files/Spam.png", 'rb') as file:
 message.add_attachment(file.read(), maintype="application", subtype="octet-stream",filename="Files/Spam.png")

with smtplib.SMTP('127.0.0.1', 30000) as server:
    server.sendmail("noa@gmail.com", "nitzan@gmail.com", message.as_string())
    server.quit()