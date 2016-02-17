"""
birthday.py
Author: Glen
Credit: Fletcher
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day


name = str(input("Hello, what is your name? "))
month = str(input("Hello {0} , what was the name of the month you were born in? ".format(name)))
#monthNum = month_name[month]
year = int(input("And what year were you born in, {0}? ".format(n)))
day = int(input("And the day? "))
age = str

print(monthNum)

if year < 1980:
    age = "stone age"
elif year <=1989:
    age = "eighties"
elif year <=1999:
    age = "nineties"
else:
    age = "two thousands"
"""
if month < 1980:
    season = "spring"
elif month <=1989:
    season = "summer"
elif month <=1999:
    season = "fall"
else:
    season = "winter" 
"""

    
    
    
    