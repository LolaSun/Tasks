"""
You're interviewing to join a security team. They want to see you build a password evaluator for your technical 
interview to validate the input. 
 
Task:  
Write a program that takes in a string as input and evaluates it as a valid password. The password is 
valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'),
and a length of at least 7 characters. 
If the password passes the check, output 'Strong', else output 'Weak'. 
 
Input Format: 
A string representing the password to evaluate. 
 
Output Format: 
A string that says 'Strong' if the input meets the requirements, or 'Weak', if not. 
 
Sample Input:  
Hello@$World19 
 
Sample Output:  
Strong
"""
str=input()
sim=('!', '@', '#', '$', '%', '&', '*')
sum=len(str)
dig=0
spec=0
for i in str:
    if i.isdigit():
        dig+=1
    elif i in sim:
        spec+=1
    
if sum>=7 and dig>=2 and spec>=2:
    print('Strong')
else:
    print("Weak")
