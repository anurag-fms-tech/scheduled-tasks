import os
import datetime as dt
from operator import index
import random

import pandas as pd
from pandas.core.methods.to_dict import to_dict

today = dt.datetime.now()
month = today.month
day = today.day
name = ""
email = ""

file = pd.read_csv("birthdays.csv")
file_dict = to_dict(file)

for i in file_dict['month']:
    if file_dict['month'][i] == month and file_dict['day'][i] == day:
        name = file_dict['name'][i]
        email = file_dict['email'][i]


templates = []
with open("letter_templates/letter_1.txt") as letter:
    t1 = letter.read()
    templates.append(t1)

with open("letter_templates/letter_2.txt") as letter:
    t2 = letter.read()
    templates.append(t2)

with open("letter_templates/letter_3.txt") as letter:
    t3 = letter.read()
    templates.append(t3)

message = random.choice(templates)
message = message.replace("[NAME]", name)

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

import smtplib
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=email,
        msg=f"Subject: Happy Birthday {name}!\n\n{message}"
    )
