import smtplib
import datetime as dt
import random

EMAIL_SENDER = "ateya.techstar@gmail.com"
EMAIL_RECEIVER = "ateya.api@gmail.com"
PASSWORD = "password"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as file:
        all_quotes = file.readlines() #read each line of quoute
        random_quote = random.choice(all_quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL_SENDER,PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER, to_addrs=EMAIL_RECEIVER,
                            msg=f"Subject: Monday Motivation\n\n{random_quote}")



