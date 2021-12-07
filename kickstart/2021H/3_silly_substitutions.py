'''
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
'''

def sub_count_n2(T):
  hv_update = True

  while hv_update:
    hv_update = False
    new_s = ''
    start = 0
    while start < len(T):
      t0 = int(T[start])
      if start == len(T) -1: # last char
        new_s += T[-1]
        break
      t1 = int(T[start + 1])
      if t0 + 1 == t1 or (t0 == 9 and t1 == 0):
        new_s += str((t1+1)%10)
        hv_update = True
        start += 2
      else:
        new_s += T[start]
        start += 1
    T = new_s
  return new_s 

def sub_count_n(T):
  hv_update = True

  while hv_update:
    hv_update = False
    new_s = ''
    start = 0
    while start < len(T):
      t0 = int(T[start])
      if start == len(T) -1: # last char
        new_s += T[-1]
        break
      t1 = int(T[start + 1])
      if t0 + 1 == t1 or (t0 == 9 and t1 == 0):
        new_s += str((t1+1)%10)
        hv_update = True
        start += 2
      else:
        new_s += T[start]
        start += 1
    T = new_s
  return new_s 

# n = int(input())
# for i in range(n):
#   l = input()
#   s = input()
#   print("Case #{}: {}".format(i+1, sub_count_n(s)))

if __name__  == "__main__":
  testcases = [
    ("012", "22"),
    ("0145", "26"),
    ("00000", "00000"),
    ("98765432101", "1"),
    ("01", "2"),
    ("12", "3"),
    ("23", "4"),
    ("34", "5"),
    ("45", "6"),
    ("56", "7"),
    ("67", "8"),
    ("78", "9"),
    ("89", "0"),
    ("90", "1"),
    ("9876543210101", "3"),
    ("54321014876", "74876"),
    ("010101010101", "222222"),
    ("011201120112011201120112", "444444"),
  ]
  for testcase in testcases:
    s, ans = testcase
    result = sub_count_n(s)
    print("correct" if  result == ans else "incorred: {} expected: {}, but {}".format(s, ans,result))