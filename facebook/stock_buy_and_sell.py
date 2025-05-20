import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def bestDaysToBuyAndSell(arr):
  # Write your code here
  buy_d = 0
  sell_d = 0

  poss_buy_d = 0
  poss_sell_d = 0

  for i in range(len(arr)):
    if arr[i] < arr[poss_buy_d]:
      poss_buy_d = i

    if arr[i] >= arr[poss_sell_d]:
      poss_sell_d = i

    if poss_sell_d > poss_buy_d and arr[poss_sell_d] - arr[poss_buy_d] > arr[sell_d] - arr[buy_d]:
      buy_d = poss_buy_d
      sell_d = poss_sell_d


  return [buy_d, sell_d]




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

def printMultipleIntegerList(array):
  for j in range(len(array)):
    if j != 0:
      print(' or ', end='')
    size = len(array[j])
    print('[', end='')
    for i in range(size):
      if i != 0:
        print(', ', end='')
      print(array[j][i], end='')
    print(']', end='')


test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if output in expected:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printMultipleIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [100,180,260,310,40,535,695]
  expected_1 = [[4, 6]]
  output_1 = bestDaysToBuyAndSell(test_1)
  check(expected_1, output_1)

  test_2 = [4,2,2,2,4]
  expected_2 = [[1, 4],[2, 4],[3, 4]]
  output_2 = bestDaysToBuyAndSell(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  test_3 = [100,180,310,40,100,150]
  expected_3 = [[0, 2]]
  output_3 = bestDaysToBuyAndSell(test_3)
  check(expected_3, output_3)
