"""
You need to decompress text. The compressed version has a number next to each symbol/letter, 
representing the amount of time that symbol should appear.  
For example, a2b3 is the compressed version of aabbb 
 
Task:  
Write a program that takes the compressed text as input and outputs the decompressed version. 
 
Input Format:  
A single string with letters/symbols, each followed by a number. 
 
Output Format:  
A string, representing the decompressed text. 
 
Sample Input:  
k2&4b1 
 
Sample Output:  
kk&&&&b
"""

import re
string=input()
pattern=r"(.)([0-9]+)"
lett=re.findall(pattern, string)
lett2=[]
for i in range(len(lett)):
    lett2.append(lett[i][0]*int(lett[i][1]))

print("".join(lett2))
