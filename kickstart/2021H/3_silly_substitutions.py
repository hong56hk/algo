'''
https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
'''

def n2(s):
  while True:
    previous = s
    s = s.replace('01', '2')\
      .replace('12', '3')\
      .replace('23', '4')\
      .replace('34', '5')\
      .replace('45', '6')\
      .replace('56', '7')\
      .replace('67', '8')\
      .replace('78', '9')\
      .replace('89', '0')\
      .replace('90', '1')
      
    if s == previous:
      return s

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


# n = int(input())
# for i in range(n):
#   l = input()
#   s = input()
#   print("Case #{}: {}".format(i+1, sub_count_n(s)))

def count(s):
  # cols = 10
  # rows = len(s)
  # arr = [[None for i in range(cols)] for j in range(rows)]
  
  for i in range(len(s)):
    c0 = s[i]
    c1 = s[i+1]


  
count("Hello")

# if __name__  == "__main__":
#   testcases = [
#     ("012", "22"),
#     ("0145", "26"),
#     ("00000", "00000"),
#     ("98765432101", "1"),
#     ("01", "2"),
#     ("12", "3"),
#     ("23", "4"),
#     ("34", "5"),
#     ("45", "6"),
#     ("56", "7"),
#     ("67", "8"),
#     ("78", "9"),
#     ("89", "0"),
#     ("90", "1"),
#     ("9876543210101", "3"),
#     ("54321014876", "74876"),
#     ("010101010101", "222222"),
#     ("011201120112011201120112", "444444"),
#     ("901201", "9222"),
#     ("01357990", "2"),
#   ]
#   for testcase in testcases:
#     s, ans = testcase
#     result = n2(s)
#     print("correct" if  result == ans else "incorred: {} expected: {}, but {}".format(s, ans,result))