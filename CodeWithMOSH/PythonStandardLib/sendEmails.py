from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from re import template
from string import Template
import smtplib

Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "USCIS"
message["to"] = "ateya.api@gmail.com"
message["subject"] = "Your Masters hearing reminder"

body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("mosh.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ateyaterence@gmail.com", "rajeihikmidnriwl")
    smtp.send_message(message)
    print("Sent...")
