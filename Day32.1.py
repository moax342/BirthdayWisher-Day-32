from random import choice
import smtplib
import datetime as dt

# Day 32.1 exercise monday quotas
email = "sample@gmail.com"
password = "123456789"
to_email = "example@gmail.com"

with open("quotes.txt") as quotas:
    quotas_list = quotas.readlines()

if dt.datetime.now().weekday() == 0:

    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        connection.login(email, password)

        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=f"Subject:Monday Motivation\n\n{choice[quotas_list]}",
        )
