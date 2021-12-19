from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  s = sorted(S)
  # (E - S - 1 - K) / (1 + K)
  def countfunc(space, k):
    return int(space / (1+k))

  count = 0
  if M > 0:
    for i in range(M):
      x = s[i]
      if i == 0: # start
        count += countfunc( (x-1), K)
      else: # middle
        count += countfunc( (x-s[i-1] - 1 - K), K)
      
      if i == M - 1: # end
        count += countfunc( N-x, K)
  else:
    count = countfunc(N, K)
      
  return count

testcases = [
  (10, 1, 2, [2,6], 3),
  (15, 2, 3, [11,6,14], 1),
  (1, 2, 1, [1], 0),
  (10, 1, 10, [1,2,3,4,5,6,7,8,9,10], 0),
  (10, 1, 2, [1,10], 3),
  (10, 1, 2, [1,9], 3),
  (10, 1, 2, [1,8], 3),
  (10, 1, 2, [2,10], 3),
  (10, 1, 0, [], 5),
  (3, 1, 1, [2], 0),
  (3, 3, 1, [2], 0),
  (10, 3, 1, [4], 1),
]

for tc in testcases:
  N,K,M,S, exp_ans = tc
  ans = getMaxAdditionalDinersCount(N,K,M,S)
  print("correct" if ans == exp_ans else "incorrect: {}, expected: {} but got {}".format(S, exp_ans, ans)) 
