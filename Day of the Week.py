"""
You receive a date and need to know what day of the week it is.  
  
Task:  
Create a program that takes in a string containing a date, and outputs the day of the week. 
 
Input Format:  
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format. 
 
Output Format:  
A string containing the day of the week from the provided date. 
 
Sample Input:  
11/19/2019 
 
Sample Output:  
Tuesday
"""

from datetime import datetime
import calendar
st_date = input()
try:
    my_date=datetime.strptime(st_date, "%m/%d/%Y")
except:
    my_date=datetime.strptime(st_date, "%B %d, %Y")
weekday=calendar.day_name[my_date.weekday()]
 
print(weekday)
