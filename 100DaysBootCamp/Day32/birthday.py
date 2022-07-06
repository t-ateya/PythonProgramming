from datetime import datetime
import pandas

today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")

