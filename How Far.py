"""
You are walking from your house to a pond that is down your street.  
How many blocks over will you have to walk until you get to the pond? 
 
Task:  
Evaluate how many blocks you will have to walk if you are given a representation of your street where H represents your house, P represents the pond,
and every B represents a block in between the two. 
 
Input Format:  
A string of letters representing your house, the pond, and blocks on your street. 
 
Output Format:  
An integer value that represents the number of blocks between your house and the pond. 
 
Sample Input:  
BBHBBBBPBBB 
 
Sample Output:  
4
"""

import re
map=input()
pattern=r"(H|P)(B*)(H|P)"
dist=len(re.search(pattern, map).group(2))
print(dist)
