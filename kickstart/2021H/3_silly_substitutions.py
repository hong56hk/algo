
def sub_count(T):
  hv_update = True

  while hv_update:
    hv_update = False
    new_s = ''
    start = 0
    while start < len(T):
      t0 = int(T[start])
      if start == len(T) -1:
        new_s += T[-1]
        break
      t1 = int(T[start + 1])
      if t0 + 1 == t1:
        new_s += str(t1+1)
        hv_update = True
        start += 2
      elif t0 == 9 and t1 == 0:
        new_s += '0'
        hv_update = True
        start += 2
      else:
        new_s += T[start] + T[start + 1]
        start += 1
    T = new_s
  return new_s 

if __name__  == "__main__":
  testcases = [
    ("012", "22"),
    ("0145", "26"),
    ("00000", "00000"),
    ("98765432101", "1"),
  ]
  for testcase in testcases:
    s, ans = testcase
    result = sub_count(s)
    print("correct" if  result == ans else "incorred: {} expected: {}, but {}".format(s, ans,result))