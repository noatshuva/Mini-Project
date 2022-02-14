import smtplib
from email.message import EmailMessage

# This client sends a mail with a redirect URL

message = EmailMessage()
message['From'] = "noa@gmail.com"
message['To'] = "nitzan@gmail.com"
message['Subject'] = "Mini Project"

body = "Hi Nitzan,\n" \
       "I've been working on our project and found out some interesting things.\n" \
       "You can use this link to see what I found: https://www.fb.com\n" \
       "Looking forward to hear from you :)"
message.set_content(body)

with smtplib.SMTP('127.0.0.1', 30000) as server:
    server.sendmail("noa@gmail.com", "nitzan@gmail.com", message.as_string())
    server.quit()