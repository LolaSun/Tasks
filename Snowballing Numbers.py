"""
You are given a list of numbers in a particular order. You need to check to see if each number is greater than the sum of all the previous number of the list.   
If they are, you have created successful snowball numbers. 
 
Task:  
Create a program that takes in an array of numbers, check if each number is greater than the sum of all previous numbers, and output true if the condition is met, and false, if not. 
 
Input Format:  
The first input denotes the length of the list (N). The next N lines contain the list elements as integers.  
 
Output Format:  
A string, true or false. 
 
Sample Input:  
4 
1 
3 
7 
58 
 
Sample Output:  
true
"""

nums=int(input())
dig=[int(input()) for i in range(nums)]
summ=0
for i in dig:
    if i>summ:
        summ+=i
    else:
        print("false")
        break
else:
    print("true")