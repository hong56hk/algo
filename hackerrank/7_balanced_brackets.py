#!/bin/python3
'''
https://www.hackerrank.com/challenges/balanced-brackets/problem

  *Checking Bracket Pairs

There are tree types of Brackets which are round brackets (), square brackets [], and curly brackets {} in each line.
Write a program to read a line and determine whether is it syntactically correct.

Example 1: Valid input
{}[]()

Example 2: Valid input
{([()]())}

Example 3: Invalid input
{[}

Example 4: Invalid input
{[(])}

Sample input:
{}[]()
{([()]())}
{[}
{[(])}

Sample output:
YES
YES
NO
NO

'''

from collections import deque
import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
  q = []  # use as stack
  for c in s:
    if c in ["(", "[", "{"]:
      q.append(c)
    elif c in [")", "]", "}"]:
      if len(q) == 0:
        return "NO"
      open_b = q.pop()
      if (open_b != "(" and c == ")") or \
        (open_b != "[" and c == "]") or \
        (open_b != "{" and c == "}"):
        return "NO"
    else:
      print("unexpected input")
      return "NO"

  if len(q) == 0:
    return "YES"
  else:
    return "NO"

  

if __name__ == '__main__':
  # test case 1: 
  print(isBalanced("{{{{"))       # NO
  print(isBalanced("]]]]]"))       # NO
  print(isBalanced("{}[]()"))       # YES
  print(isBalanced("{([()]())}"))   # YES
  print(isBalanced("{[}"))          # NO
  print(isBalanced("{[(])}"))       # NO
  print(isBalanced("{{([])}}"))     # YES
  print(isBalanced("{{)[](}}"))     # NO
  print(isBalanced("{[()]}"))       # YES
  print(isBalanced("{[(])}"))       # NO
  print(isBalanced("{{[[(())]]}}"))       # YES

