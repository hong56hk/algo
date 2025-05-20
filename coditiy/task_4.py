import re


def remove_sub_question(s):
    for i in range(len(s)-1, 0 , -1):
        if s[i].isdigit():
            return s[:i+1]
    return s



def solution(T, R):
    grouped = {}

    for i in range(len(T)):
        test = T[i]
        testname = remove_sub_question(test)

        if R[i] == "OK":
            if testname in grouped:
                grouped[testname] = True and grouped[testname]
            else:
                grouped[testname] = True
        else:
            grouped[testname] = False

    score = 0
    for v in grouped.values():
        if v:
            score += 1
    return score  * 100  // len(grouped.values())


testcases = [
    (["test1a", "test2", "test1b", "test1c" ,"test3"],
     ["Wrong answer", "OK", "Runtime error", "OK", "Time limit exceeded"], 33),

    (["codility1", "codility3", "codility2", "codility4b" ,"codility4a"],
     ["Wrong answer", "OK", "OK", "Runtime error", "OK"], 50),
]
print("Testing...")
for T, R, ans in testcases:
    re = solution(T, R)
    if (ans == re):
        print("PASSED")
    else:
        print( f"FAILED: {T} {R} ans: {ans} != {re}")
