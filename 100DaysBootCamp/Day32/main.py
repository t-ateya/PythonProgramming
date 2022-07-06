
import smtplib
my_email = "ateyaterencearrey@gmail.com"
password = "Determined2Learn"
receiver = "ateya.api@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:# email provider
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=receiver,
                        msg="Subject:Hello\n\nThis is the body of my email")

