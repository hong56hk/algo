# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, K):
    # Implement your solution here
    D = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6,
    }
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    d = K + D[S]
    return week[d%7]

testcases = [
    ("Wed", 2, "Fri"),
    ("Sat", 23, "Mon"),
]
for s, k, a in testcases:
    re = solution(s, k)
    if (a == re):
        print("PASSED")
    else:
        print( "FAILED: {} {} {} != {}".format(s, k, a, re))
