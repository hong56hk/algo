# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque
from bisect import bisect_left, bisect_right

def solution_1(A, K):
    # Implement your solution here
    min_amp = float('inf')

    for i in range(len(A) - K + 1):
        remaining = A[:i] + A[i+K:]
        diff = max(remaining) - min(remaining)
        if diff < min_amp:
            min_amp = diff

    return min_amp

def solution(A, K):
    # Implement your solution here
    min_diff = float('inf')

    full_sort_a = A.copy()
    full_sort_a.sort()
    for i in range(len(A) - K + 1):
        sort_a = full_sort_a.copy()
        for k in range(K):
            v = A[i+k]
            bisect_left(sort_a, v)
            sort_a.pop(bisect_left(sort_a, v))

        diff = sort_a[-1] - sort_a[0]
        if diff < min_diff:
            min_diff = diff
    return min_diff



testcases = [
    ([5,3,6,1,3], 2, 2),
    ([8,8,4,3], 2, 0),
    ([3,5,1,3,9,8], 4, 1),
]
print("Testing...")
for a, k, ans in testcases:
    re = solution(a, k)
    if (ans == re):
        print("PASSED")
    else:
        print( "FAILED: {} K:{},  ans: {} != {}".format(a, k, ans, re))
