#!/bin/python3

'''
In a computer security course, you just learned about password decryption. 
Your fellow student has created their own password encryption method, and they've asked you to test how secure it is. 
Your task is to recover the original password given the encrypted password provided to you by your classmate.

At first, it seems impossible. But one day after class, you catch a peek of your classmate's notebook where the encryption 
process is noted. You snap a quick picture of it to reference later. It says this:

Given string s, let s[i] represent the i-th character in the string s, using 0-based indexing.

1. Initially i = 0.
2. If s[i] is lowercase and the next character s[i+1] is uppercase, swap them, add a '*' after them, and move to i+2.
3. If s[i] is a number, replace it with 0, place the original number at the start, and move to i+1.
4. Else, move to i+1.
5. Stop if i is more than or equal to the string length. Otherwise, go to step 2.
There's even an example mentioned in the notebook. When encrypted, the string "hAck3rr4nk" becomes "43Ah*ck0rr0nk". (Note: the original string, "hAck3rr4nk", does not contain the character 0.)

# Note:
- The original string always contains digits from 1 to 9 and does not contain 0.
- The original string always contains only alpha-numeric characters.
 
Using this information, your task is to determine the original password (before encryption) when given the encrypted password from your classmate.

# Function Description
Complete the function decryptPassword in the editor below. decryptPassword must return the original password string before it was encrypted by your classmate.

decryptPassword has the following parameter:
  s:  the password string after it was encrypted by your classmate

# Constraints

- 1 <= length of s <= 105
- s can contain Latin alphabet characters (a-z, A-Z), numbers (0-9), and the character '*'.

Input Format For Custom Testing
  The first line contains the password string obtained after it was encrypted by your classmate.

Sample Case 0
  Sample Input For Custom Testing
    51Pa*0Lp*0e
  Sample Output
    aP1pL5e
  Explanation
    If we apply the sequence of operations on the string aP1pL5e, we get the string 51Pa*0Lp*0e.

We start at the letter a since i = 0.
Since a is lowercase and the next character P is uppercase, we swap them, add a '*' after, and move to the next designated character (i+2). So currently it is Pa*1pL5e.
Now we're on the character 1. This is a number, so we replace it with 0, put the original number 1 at the start, and continue to the next character (i+1). Now it is 1Pa*0pL5e.
We're still in the middle of the string (i does not equal the string length), so we repeat the process again.
 
After that, 1Pa*0pL5e becomes 1Pa*0Lp*5e. Then, 1Pa*0Lp*5e becomes 51Pa*0Lp*0e. Since e is at the end of the string, it can't be swapped with the next character. 
Thus, aP1pL5e becomes 51Pa*0Lp*0e when encrypted.

Sample Case 1
Sample Input For Custom Testing

pTo*Ta*O
Sample Output

poTaTO
Explanation

If we apply the sequence of operations on the string poTaTO, we get the string pTo*Ta*O.

We start at the letter p since i = 0.
The character p is lowercased, but the next character is also lowercased. So there's no need to swap them.
We move on to the next character (i+1), which is o. Now, since o is followed by capital T, we swap them, add a '*' after, and move to the next designated 
character (i+2). So currently it is pTo*aTO.
Moving to character a, it is followed by a capitalized letter, so we likewise swap these, add a '*' after, and move to i+2. Now it is pTo*Ta*O.
O is at the end of the string, we stop there.
 

Thus, poTaTO becomes pTo*Ta*O when encrypted.

'''
import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
  # Write your code here
  skip_count = 0
  digit_q = []
  pwd = ''
  for i in range(len(s)):
    if skip_count > 0:
      skip_count -= 1
      continue
    c = s[i]
    if c == '0':
      pwd += digit_q.pop()
    elif c.isalpha() and c.isupper() and i+2 < len(s) and s[i+1].islower and s[i+2] == '*':
      pwd += s[i+1] + s[i]
      skip_count = 2 # skip next two
    elif c.isdigit():
      digit_q.append(c)
    else:
      pwd += c
  return pwd



if __name__ == '__main__':
  e_pwd = "43Ah*ck0rr0nk"
  pwd = decryptPassword(e_pwd)

  print(pwd)