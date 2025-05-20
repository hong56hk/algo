import heapq
import random

def test():
  heap = []
  for i in range(10):
    heap = [random.randint(1,100) for _ in range(100)]

  print(heap)

  h = heapq.heapify(heap)
  print(heap)
  print(h)
  print(type(heap))

test()
