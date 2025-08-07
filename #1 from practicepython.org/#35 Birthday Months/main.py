#imports
import json
from collections import Counter
from datetime import datetime


# read json 

with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#35 Birthday Months/Birth.json', 'r') as file:
    birthdays = json.load(file)


months = []
# extract months from birthdays
for name, date_str in birthdays.items():
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")  # parse to date
        month_name = date.strftime("%B")  # convert month number to full name
        months.append(month_name)
    except ValueError:
        print(f"⚠️ Skipping invalid date for {name}: {date_str}")

# count occurrences of each month
month_counts = Counter(months)

print("Birthday Month Counts:", month_counts)