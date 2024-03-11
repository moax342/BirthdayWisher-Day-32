##################### Extra Hard Starting Project ######################

import random
import pandas
import smtplib
import datetime as dt

EMAIL = "sample@gmail.com"
PASSWORD = "#1425379816738"

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_list = birthdays_data.to_dict(orient="records")

chosen_message = random.choice([1, 2, 3])
with open(f"letter_templates/letter_{chosen_message}.txt") as message:
    new_message = message.read()

# 2. Check if today matches a birthday in the birthdays.csv
for _ in range(0, 2):
    if dt.datetime.now().month == birthdays_list[_]["month"] and dt.datetime.now().day == birthdays_list[_]["day"]:
        with smtplib.SMTP("localhost",2025) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=f"Subject:HappyBirthDay\n\n "
                                    f"{new_message.replace('[NAME]', birthdays_list[_]['name'])}"
                                )
