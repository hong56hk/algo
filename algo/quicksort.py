'''

Implementation of quicksort

https://en.wikipedia.org/wiki/Quicksort

'''


def partition(arr, s, e):
  np = s # new pivot position
  p = e # pivot = last element
  pv = arr[p]

  for i in range(s, e):
    if arr[i] < pv:
      arr[i], arr[np] = arr[np], arr[i]
      np += 1

  arr[np], arr[p] = arr[p], arr[np]
  return np


def quicksort(arr, s=0, e=None):
  e = len(arr)-1 if e is None else e
  
  if s < e:
    p = partition(arr, s, e)

    quicksort(arr, s, p-1)
    quicksort(arr, p+1, e)
  


if __name__ == '__main__':
  testcases = [
    [5],
    [1,2],
    [1,2,3],
    [1,2,3,4,5,6,7,8,9,10],
    [1,1,1,1,1,1,1],
    [7,1,2],
    [2,1,3,7,6,4],
    [1,556,24,5,35,4,6,7,8,1,235],
  ]
  
  for i in range(len(testcases)):
    tc = testcases[i]
    tc1 = tc.copy()
    tc2 = tc.copy()
    
    quicksort(tc1)
    
    tc2.sort()
    if tc2 != tc1:
      print("incorrect {}".format(tc))
      print("expected {}".format(tc2))
      print("actual {}".format(tc1))
    else:
      print("testcase [{}] passed".format(i))
  
  
