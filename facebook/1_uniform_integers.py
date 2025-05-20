'''

find the number of uniform integer in between A and B
uniform interger is all the digitals in the number are the same
ie 1111,2222,3333

'''

# Write any import statements here
import math

def dig_count(n):
  return int(math.log(n, 10))+1

def first_dig(i):
  d_count = dig_count(i)
  return int(i/(10**(d_count-1)))

def nearest_greater_uni_int(i):
  d_count = dig_count(i)
  left_dig = int(i/(10**(d_count-1)))
  return int(str(left_dig)*d_count)

def uniform_int_count(A: int, B: int) -> int:
  count = 0

  a_uni_int = nearest_greater_uni_int(A)
  b_uni_int = nearest_greater_uni_int(B)

  # part 1: start to start + 1 dig
  dig_diff = dig_count(B) - dig_count(A)
  if dig_diff > 0:
    part_1 = 10 - first_dig(A) 
    if A > a_uni_int:
      part_1 -= 1
    
    # between
    part_2 = max(9 * (dig_diff-1), 0)

    # part 3: end - 1 dig to end
    part_3 = first_dig(B)
    if B < b_uni_int:
      part_3 -= 1

    count = part_1 + part_2 + part_3

  else:
    count = first_dig(B) - first_dig(A) + 1
    if A > nearest_greater_uni_int(A):
      count -= 1
    if B < nearest_greater_uni_int(B):
      count -= 1
  
  return count

if __name__ == "__main__":
  testcases = [
    [(75, 300), 5],
    [(1, 9), 9],
    [(999999999, 999999999), 1],
    [(1, 10), 9],
    [(1, 100), 18],
    [(1, 1000), 27],
    [(77, 100), 3],
    [(66, 2221), 14],
    [(66, 8887), 20],
    [(66, 8888), 21],
    [(66, 8889), 21],
  ]
  for i in range(len(testcases)):
    tc = testcases[i]
    input = tc[0]
    ans = tc[1]
    result = uniform_int_count(input[0], input[1])
    ans = tc[1]
    if result == ans:
      print("testcase #{} passed".format(i))
    else:
      print("testcase #{} failed. expected: {} , but got: {}".format(i, ans, result))