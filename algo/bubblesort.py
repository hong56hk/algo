'''

Implementation of bubble sort

https://en.wikipedia.org/wiki/Bubble_sort

'''


def bubblesort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  
  

if __name__ == '__main__':
  testcases = [
    [7,1,2],
    [2,1,3,7,6,4],
    [1,556,24,5,35,4,6,7,8,1,235],
  ]
  
  for tc in testcases:
    tc2 = tc.copy()
    print(tc)
    bubblesort(tc)
    print("my {}".format(tc))

    tc2.sort()
    print("ct {}".format(tc2))
  
  
