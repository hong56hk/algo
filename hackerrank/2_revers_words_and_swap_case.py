#!/bin/python3

'''
1. Python: Reverse Words and Swap Cases

Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those 
words but in the reverse order and such that all cases of letters in the original string are swapped, i.e. lowercase letters become 
uppercase and uppercase letters become lowercase.


Example

sentence = "rUns dOg"
Reverse the word order and swap the case of all letters, then return the string "DoG RuNS".



Function description
Complete the function reverse_words_order_and_swap_cases in the editor below.



The function has the following parameter(s):
    string sentence: a given string of space-separated words

Returns:
    string : a string containing all the words from the sentence but in the reverse order and such that all cases of letters in the sentence string are swapped.

 

Constraints
- sentence contains only English letters and spaces.
- sentence begins and ends with a letter.
- There are no two consecutive spaces in sentence.
- There are at most 10 words in sentence.
- The lengths of each of the words is at most 10.
 
Input Format Format for Custom Testing
Sample Case 0
Sample Input

STDIN                 Function 
-----                 -------- 
aWESOME is cODING  →  sentence = "aWESOME is cODING"

 
Sample Output

Coding IS Awesome


'''

#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    ss = sentence.swapcase().split(" ")
    ss.reverse()
    return " ".join(ss)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # sentence = input()

    # result = reverse_words_order_and_swap_cases(sentence)

    # fptr.write(result + '\n')

    # fptr.close()
    print(reverse_words_order_and_swap_cases("aWESOME is cODING"))