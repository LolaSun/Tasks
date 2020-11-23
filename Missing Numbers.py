"""
You are given a list of whole numbers in ascending order. You need to find which numbers are missing in the sequence. 
 
Task:  
Create a program that takes in a list of numbers and outputs the missing numbers in the sequence separated by spaces. 
 
Input Format:  
The first input denotes the length of the list (N). The next N lines contain the list elements as integers.  
 
Output Format:  
A string containing a space-separated list of the missing numbers. 
 
Sample Input:  
5 
2 
4 
5 
7 
8 
 
Sample Output:  
3 6
"""

num=int(input())
nums=[int(input()) for i in range(num)]
nums2=[]
for i in range(len(nums)):
    try:
        ii=1
        while nums[i]+ii!=nums[i+1]:
            nums2.append(str(nums[i]+ii))
            ii += 1
            
    except:
        pass

print(" ".join(nums2))
