#!/bin/python3
'''

A demostration on heap implementation. The heap can be used as priority queue.

FOR DEMOSTRATION PURPOSE. THIS IS NOT OPTIMIZED.

For production use, please use heapq.


'''
class PrioritedItem():
  def __init__(self, priority, value):
    self.priority = priority
    self.value = value
  
  def __str__(self):
    return str(self.value)

class Heap():
  def __init__(self, priority=0, value=None):
    self.data_arr = []
    
    if value:
      self.insert(priority, value)

  def __str__(self):
    ss = []
    for item in self.data_arr:
      ss.append("({}, {})".format(item.priority, item.value))
    
    return " ".join(ss)
  
  # return the parent of node in pos
  def parent(self, pos):
    return int((pos+1)/2)-1

  def left(self, pos):
    return (pos+1)*2-1

  # return the right child of node in pos
  def right(self, pos):
    return (pos+1)*2

  def insert(self, priority, value):
    self.data_arr.append(None)  # prepare a hole
    hole_pos = len(self.data_arr) - 1
    parent_pos = self.parent(hole_pos)
    
    while True:
      if hole_pos == 0:
        self.data_arr[hole_pos] = PrioritedItem(priority, value)
        break

      parent_item = self.data_arr[parent_pos]
      if parent_item.priority <= priority:
        self.data_arr[hole_pos] = PrioritedItem(priority, value)
        break
      else: # percolate
        self.data_arr[hole_pos] = parent_item
        hole_pos = parent_pos
        parent_pos = self.parent(hole_pos)

    return hole_pos

  # return the hightest priority object, 
  # ie smallest value in priority field
  def dequeue(self):
    hole_pos = 0

    return_item = self.data_arr[hole_pos]
    remove_item = self.data_arr.pop()
    
    while True:
      left_child = self.data_arr[self.left(hole_pos)]
      right_child = self.data_arr[self.right(hole_pos)]
      smaller_child_pos = self.left(hole_pos) if left_child.priority <= right_child.priority else self.right(hole_pos)
    
      if self.data_arr[smaller_child_pos].priority >= remove_item.priority:
        self.data_arr[hole_pos] = remove_item
        break
      else:
        self.data_arr[hole_pos] = self.data_arr[smaller_child_pos]
        hole_pos = smaller_child_pos
        if self.left(hole_pos) > len(self.data_arr) or self.right(hole_pos) > len(self.data_arr):
          self.data_arr[hole_pos] = remove_item
          break
        else:
          self.data_arr[hole_pos] = None
    
    return return_item
          


if __name__ == '__main__':
  h = Heap()
  h.insert(13, 13)
  h.insert(21, 21)
  h.insert(16, 16)
  h.insert(24, 24)
  h.insert(31, 31)
  h.insert(19, 19)
  h.insert(68, 68)
  h.insert(65, 65)
  h.insert(26, 26)
  h.insert(32, 32)

  print(h)
  h.insert(14, 14)
  print(h)

  # test for dequeue
  h2 = Heap()
  h2.insert(13, 13)
  h2.insert(14, 14)
  h2.insert(16, 16)
  h2.insert(19, 19)
  h2.insert(21, 21)
  h2.insert(19, 19)
  h2.insert(68, 68)
  h2.insert(65, 65)
  h2.insert(26, 26)
  h2.insert(32, 32)
  h2.insert(31, 31)

  print(h2)
  h2.dequeue()
  print(h2)
  