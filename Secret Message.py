"""
You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with 
its corresponding letter in a backwards version of the alphabet.  
What do your messages look like? 
 
Task:  
Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the 
English alphabet. 
 
Input Format:  
A string of your message in its normal form. 
 
Output Format:  
A string of your message once you have encoded it (all lower case). 
 
Sample Input:  
Hello World 
 
Sample Output:  
svool dliow
"""

import string

input_words = input()
eng_letters = string.ascii_lowercase 

new_string = ''
for letter in input_words:
    letter_lowercase = letter.lower()
    if letter_lowercase in eng_letters:
        letter_index = eng_letters.index(letter_lowercase)
        reverse_index = -(letter_index + 1)

        new_string += eng_letters[reverse_index]
    elif letter == ' ':
        new_string += letter

print(new_string)
