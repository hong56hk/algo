#!/bin/python3
'''

Given an array containing numbers. Group the array of numbers into two sets, the larger set and the smaller set in which

1. The largest set should contain minimal number of numbers
2. The number is either in the largest set or smaller set, not both
3. The sum of largest set is always greater than that of the smaller set

Retun the largest set.

'''

from collections import deque
import math
import os


def minimalHeaviestSetA(arr):
    # Write your code here
    set_a = []
    
    weight_a = 0
    weight_b = 0
    
    arr.sort()
    remain_items = deque(arr)

    while len(remain_items) > 0:
        if weight_a <= weight_b:
            max = remain_items.pop()
            weight_a += max
            set_a.append(max)
        else:
            min = remain_items.popleft()
            if weight_a <= weight_b + min:
                if len(remain_items) >= 1:
                    max = remain_items.pop()
                    weight_a += max
                    set_a.append(max)
                    
                    weight_b += min
                else:
                    weight_a += min
                    set_a.append(min)
            else:
                weight_b += min
    set_a.sort()
    return set_a

if __name__ == '__main__':
    # arr = [5,3,2,4,1,2]
    # arr = [5,5,5,5,5, 5,5,5,5,5 ]
    arr = [4,2,5,1,6]

    print(minimalHeaviestSetA(arr))