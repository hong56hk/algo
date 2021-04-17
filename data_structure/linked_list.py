#!/bin/python3
'''
20210311

A thread not-safe linked-list with minimal functions

'''

class Node():
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
  
  def __str__(self):
    return str(self.value)

class LinkedList():
  def __init__(self, value=None):
    self.first = None
    self.last = None
    self.size = 0
    if value:
      self.push(value)

  def __str__(self):
    ss = ''
    n = self.first
    while n:
      ss += "{} -> ".format(n.value)
      n = n.next
    return ss[:-3]

  def peek(self, pos):
    if pos < self.size:
      if pos < self.size/2:
        n = self.first
        for _ in range(pos):
          n = n.next
        return n.value
      else:
        n = self.last
        for _ in range(self.size-pos-1):
          n = n.prev
        return n.value
    return None

  def push(self, value):
    n = Node(value)
    if self.first:
      n.prev = self.last
      self.last.next = n
      self.last = n
    else:
      self.first = n
      self.last = n
    self.size += 1
  
  def pop(self):
    n = None
    if self.last:
      n = self.last.value
      self.last = self.last.prev
      self.size -= 1
    
    return n

  # return the value at pos
  def get(self,pos=0):
    if self.size == 0:
      return None
    n = self.first
    for _ in range(pos):
      n = n.next
    if n.prev:
      n.prev.next = n.next
    if n.next:
      n.next.prev = n.prev
    self.size -= 1
    return n.value

  def insert(self, value, pos=0):
    n = Node(value)
    if self.size == 0 or pos >= self.size:
      self.push(value)
    else:
      aff_n = self.first  
      for _ in range(pos):
        aff_n = aff_n.next
      
      n.prev = aff_n.prev
      n.next = aff_n
      if aff_n.prev:
        aff_n.prev.next = n
      else: # insert at position 0
        self.first = n
      aff_n.prev = n
      
      self.size += 1
    


if __name__ == '__main__':
  l = LinkedList()
  l.push("b")
  l.push("c")
  l.insert("a")
  l.push("d")
  l.push("e")
  l.push("f")

  print(l)
  print(l.peek(4))
  print(l.get(4))
  print(l)