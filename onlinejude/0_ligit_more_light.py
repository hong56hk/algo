'''
Programming Challenges:

7.6.1 Light, More Light

PC/UVa IDs: 110701/10110

#NumberTheory

'''

def deter(n:int):
  on = False
  for i in range(1,n+1,1):
    if n%i == 0:
      on = not on
  return on

if __name__ == "__main__":
  print(deter(3))
  print(deter(6241))
  print(deter(8191))
