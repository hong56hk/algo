#!/bin/python3

'''
Complete the 'authEvents' function below.

The function is expected to return an INTEGER_ARRAY.
The function accepts 2D_STRING_ARRAY events as parameter.
'''

import math
import os
import random
import re
import sys


def hash(pwd):
    hash_v = 0
    i = len(pwd) - 1
    for c in pwd:
        hash_v += ord(c) * 131**i
        i -= 1
    return hash_v % ((10**9) + 7)

def authEvents(events):
    # Write your code here
    result = []
    pwd = None
    hash_pwd = None
    hash_pwd_0 = None
    hash_pwd_9 = None
    hash_pwd_A = None
    hash_pwd_Z = None
    hash_pwd_a = None
    hash_pwd_z = None

    for e in events:
        if e[0] == "setPassword":
            pwd = e[1]
            hash_pwd = hash(pwd)
            hash_pwd_0 = hash(pwd + "0")
            hash_pwd_9 = hash_pwd_0 + 9
            hash_pwd_A = hash_pwd_0 + 17
            hash_pwd_Z = hash_pwd_0 + 42
            hash_pwd_a = hash_pwd_0 + 49
            hash_pwd_z = hash_pwd_0 + 74
            
        else: # authorize
            in_pwd = int(e[1])
            if hash_pwd == in_pwd or ( hash_pwd_0 <= in_pwd <= hash_pwd_9 ) or ( hash_pwd_A <= in_pwd <= hash_pwd_Z) or ( hash_pwd_a <= in_pwd <= hash_pwd_z ):
                result.append(1)
            else:
                result.append(0)
    return result


if __name__ == '__main__':

    print(hash("a"))
    events = [
        ['setPassword', 'a'],
        ['authorize', '97'],
        ['authorize', '12756'],
        ['authorize', '12804'],
        ['authorize', '12829'],
    ]
    print(authEvents(events))