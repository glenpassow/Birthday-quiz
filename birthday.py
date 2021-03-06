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
month = str(input("Hi {0}, what was the name of the month you were born in? ".format(name)))

m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
a = m.index(month)
a = a + 1

year = int(input("And what year were you born in, {0}? ".format(name)))
day = int(input("And the day? "))
age = str

if a == todaymonth and day == todaydate:
    print("Happy birthday!")
else:
    
    if a == 10 and day == 31:
        print("You were born on Halloween!")
    else:

        if year < 1980:
            age = "stone age"
        elif year <=1989:
            age = "eighties"
        elif year <=1999:
            age = "nineties"
        else:
            age = "two thousands"
    


        if a <= 5 and a >= 3 :
            season = "spring"
        elif a <= 8 and a >= 6 :
            season = "summer"
        elif a <= 11 and a >= 9 :
            season = "fall"
        else:
            season = "winter" 
    
        print( "{0}, you are a {1} baby of the {2}.".format(name, season, age))



    
    
    
    