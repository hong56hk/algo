'''

Implementation of merge sort

https://en.wikipedia.org/wiki/Merge_sort

'''

def mergesort(arr):
  if len(arr) > 1:
    mid = int(len(arr)/2)
    
    larr = arr[:mid]
    rarr = arr[mid:]
      
    mergesort(larr)
    mergesort(rarr)

    # merge
    l = r = 0
    for c in range(len(arr)):
      if l >= len(larr): # left is empty
        arr[c] = rarr[r]
        r+=1
      elif r >= len(rarr): # righ is empty
        arr[c] = larr[l]
        l+=1
      elif larr[l] < rarr[r]:
        arr[c] = larr[l]
        l+=1
      else:
        arr[c] = rarr[r]
        r+=1
    

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
    
    mergesort(tc1)
    
    tc2.sort()
    if tc2 != tc1:
      print("incorrect {}".format(tc))
      print("expected {}".format(tc2))
      print("actual {}".format(tc1))
    else:
      print("testcase [{}] passed".format(i))
  
  
