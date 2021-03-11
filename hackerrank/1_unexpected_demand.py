#!/bin/python3

'''
2. Unexpected Demand
A widget manufacturer is facing unexpectedly high demand for its new product,. They would like to satisfy as many customers as possible. 
Given a number of widgets available and a list of customer orders, what is the maximum number of orders the manufacturer can fulfill in full?

Function Description

Complete the function filledOrders in the editor below. The function must return a single integer denoting the maximum possible number of fulfilled orders.
 
filledOrders has the following parameter(s):
    order :  an array of integers listing the orders
    k : an integer denoting widgets available for shipment


Constraints
- 1 ≤ n ≤  2 x 105
- 1 ≤  order[i] ≤  109
- 1 ≤ k ≤ 109

Input Format For Custom Testing
The first line contains an integer, n, denoting the number of orders.

Each line i of the n subsequent lines contains an integer order[i].

Next line contains a single integer k denoting the widgets available.

Sample Case 0
Sample Input For Custom Testing
2
10
30
40

Sample Output
2

Explanation
order = [10,30] with 40 widgets available. Both orders can be fulfilled.

Sample Case 1
Sample Input For Custom Testing
3
5
4
6
3

Sample Output
0

Explanation
order = [5,4,6] with 3 widgets available
None of the orders can be fulfilled.

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
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Write your code here
    order.sort()
    fc = 0
    for o in order:
        if k < o:
            return fc
        else:
            k -= o
            fc += 1
    return fc  

if __name__ == '__main__':

    order = [5,4,6]
    k = 10
    result = filledOrders(order, k)
    print(result)
