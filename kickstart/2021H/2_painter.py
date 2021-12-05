'''

https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d9a88

'''

RED = 0b001
YELLOW = 0b010
BLUE = 0b100

COLOR = {
  'U': 0b000,
  'R': RED,
  'B': BLUE,
  'Y': YELLOW,
  'O': RED | YELLOW,
  'P': RED | BLUE,
  'G': YELLOW | BLUE,
  'A': RED | YELLOW | BLUE,
}

def stroke(P:str) -> int:
  r_count = 0
  y_count = 0
  b_count = 0
  last_r = 0
  last_y = 0
  last_b = 0

  for p in P:
    cur_r = COLOR[p] & RED
    cur_y = COLOR[p] & YELLOW
    cur_b = COLOR[p] & BLUE

    r_count += 1 if last_r != cur_r and cur_r != 0 else 0
    y_count += 1 if last_y != cur_y and cur_y != 0 else 0
    b_count += 1 if last_b != cur_b and cur_b != 0 else 0
    
    last_r = cur_r
    last_y = cur_y
    last_b = cur_b

  return r_count + y_count + b_count

n = int(input())
for i in range(n):
  l = input()
  s = input()
  print("Case #{}: {}".format(i+1, stroke(s)))


# if __name__  == "__main__":
#   testcases = [
#     ("YYYYBBBBYYYY", 3),
#     ("YYGGBB", 2),
#     ("RAOR", 3)
#   ]
#   for testcase in testcases:
#     p, ans = testcase
#     result = stroke(p)
#     print("correct" if  result == ans else "incorred: {} expected: {}, but {}".format(p, ans,result))