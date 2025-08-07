#imports
import json
from collections import Counter
from datetime import datetime
from bokeh.io import show, output_file
from bokeh.plotting import figure



# read json 

with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#36 Birthday Plots/Birth.json', 'r') as file:
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


months_ordered = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


x = months_ordered
y = [month_counts.get(month, 0) for month in months_ordered]


output_file("birthday_histogram.html")

p = figure(x_range=x, title="Scientist Birthdays by Month",
           x_axis_label="Month", y_axis_label="Number of Birthdays")

p.vbar(x=x, top=y, width=0.5, color="skyblue")

show(p)
