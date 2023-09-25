import smtplib
import datetime as dt
import random

MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "..."

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Day 032/birthday-wisher/practice/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="...@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}")



