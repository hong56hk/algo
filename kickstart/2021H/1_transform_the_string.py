'''

https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008da461

'''

def transform_count(S: str, F: str) -> int: 
  cache = [None] * 26
  count = 0
  for s in S:
    pos = ord(s)-ord('a')
    if cache[pos] != None:
      count += cache[pos]
    else:
      min_t = 26 # at most 25 operations
      for f in F:
        t = abs(ord(s) - ord(f))
        if t > 13:
          t = 26 - t
        if t < min_t:
          min_t = t
      cache[pos] = min_t
      count += min_t
  return count


n = int(input())
for i in range(n):
  s = input()
  f = input()
  print("Case #{}: {}".format(i+1, transform_count(s,f)))

# if __name__  == "__main__":
#   testcases = [
#     ("z", "a", 1),
#     ("xyz", "a", 6),
#     ("abcd", "a", 6),
#     ("abcd", "d", 6),
#     ("pppp", "p", 0),

#     ("pqrst", "ou", 9),
#     ("abc", "abc", 0),
#     ("aaaaaaaaaaaaaaab", "aceg", 1),
#   ]
#   for testcase in testcases:
#     s, f, ans = testcase
#     result = transform_count(s, f)
#     print("correct" if  result == ans else "incorred: {} {} expected: {}, but {}".format(s,f,ans,result))