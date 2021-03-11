#!/bin/python3


class node():
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
  
  def __str__(self):
    return str(self.value)
class linklist():
  def __init__(self, value=None):
    self.first = None
    self.last = None
    self.size = 0
    if value:
      self.push(value)

  def push(self, value):
    n = node(value)
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
  
  def insert(self, value, pos=0):
    n = node(value)
    if self.first:
      aff_n = self.first
      if pos < self.size:
        for _ in range(pos):
          aff_n = aff_n.next
      else:
        aff_n = self.last
      
      n.prev = aff_n.prev
      n.next = aff_n
      if aff_n.prev:
        aff_n.prev.next = n
      aff_n.prev = n
      
      self.size += 1
    else:
      self.push(n)


if __name__ == '__main__':
  l = linklist()
  l.push(1)
  l.push(2)
  l.insert(0)
  l.push(4)

  print(l.pop())
  print(l.pop())
  print(l.pop())
  print(l.pop())
  print(l.pop())
  print(l.pop())