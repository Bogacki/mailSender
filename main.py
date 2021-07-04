##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas
from random import choice
import os


LOGIN = "mikolaj.python@gmail.com"
PASSWORD = os.environ.get("PASSWORD")
SERVER = "smtp.gmail.com"

letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour

birthday_people = pandas.read_csv("birthdays.csv").to_dict(orient="records")

for person in birthday_people:
    if person["month"] == month and person["day"] == day:

        print(person["year"],person["month"],person["day"])

        with open(f"./letter_templates/{choice(letters)}") as file:
            letter_msg = file.read()
            letter_msg = letter_msg.replace("[NAME]", person["name"])

        with smtplib.SMTP(SERVER) as connection:
            connection.starttls()
            connection.login(user=LOGIN, password=PASSWORD)
            connection.sendmail(
                to_addrs=person["email"],
                from_addr=LOGIN,
                msg=f"Subject: Happy Birthday! \n\n{letter_msg}")





