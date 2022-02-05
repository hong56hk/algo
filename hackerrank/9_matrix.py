#!/bin/python3

import math
import os
import random
import re
import sys




# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])
n = 7
m = 3
matrix = [
"Tsi",
"h%x",
"i #",
"sM ",
"$a ",
"#t%",
"ir!",
]

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)


result_str = ''
tmp = ''
for col in range(m):
    for row in range(n):
        c = matrix[row][col]
        if c.isalnum():
            if len(tmp) > 0:
                result_str += ' '
                tmp = ''
            result_str += c
        else:
            tmp += c
result_str += tmp

print(result_str)