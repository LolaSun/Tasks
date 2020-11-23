"""
If a sentence flows, the first letter of each word will be the same to the last letter of the previous word.  
 
Task: 
Write a program that takes in a string that contains a sentence, checks if the first letter of each word is the same as the last letter of the previous word. 
If the condition is met, output true, if not, output false.  
Casing does not matter. 
 
Input Format:  
A string containing a sentence of words. 
 
Output Format:  
A string: true or false. 
 
Sample Input: 
this string gets stuck 
 
Sample Output:  
true
"""

string=input().split(" ")
for i in range(len(string)):
    try:
        if string[i][-1]!=string[i+1][0]:
            print("false")
            break
    except IndexError:
        pass

else:
    print("true")
