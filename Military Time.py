"""
You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, 
you should output the time as it would appear on a 24 hour clock.   
 
Task:   
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock. 
 
Input Format:  
A string that includes the time, then a space and the indicator for AM or PM. 
 
Output Format:  
A string that includes the time in a 24 hour format (XX:XX) 
 
Sample Input:  
1:15 PM 
 
Sample Output:  
13:15
"""

import re
po=input()
pattern="(\d+):*(\d*)\s(\w+)"
time=re.fullmatch(pattern, po)
hours=time.group(1)
min=time.group(2)
type=time.group(3)
def yui():
    if type=="PM" and hours!="12":
        n=12
    elif type=="PM" and hours=="12":
        n=0
    elif type=="AM" and hours!="12":
        n=0
    elif type=="AM" and hours=="12":
        n=-12
    x=int(hours)+n
    if len(str(x))<2:
        x="0"+str(x)
    return x
    
    
print(yui(),":", min, sep="")
