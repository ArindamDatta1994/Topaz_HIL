import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
receiver = "arindamdatta1994@yahoo.com"

msg = EmailMessage()
msg["Subject"] = "Automated Email Reminder"
msg["From"] = email
msg["To"] = receiver
msg.set_content("Hello! This is an automated test email.")

file_path = "sample.pdf"

with open(file_path, "rb") as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)

print("Email sent successfully!")