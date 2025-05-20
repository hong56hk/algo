





def solution(T):
    candy_type_count = len(set(T))
    give = len(T) // 2

    dup_count = len(T) - candy_type_count

    return candy_type_count - max(give - dup_count, 0)






testcases = [
    ([3,4,7,7,6,6], 3),
    ([80,80,100000,80,80,80,80,80,80,123333], 3),
]
print("Testing...")
for a, ans in testcases:
    re = solution(a)
    if (ans == re):
        print("PASSED")
    else:
        print( "FAILED: {}  ans: {} != {}".format(a, ans, re))
