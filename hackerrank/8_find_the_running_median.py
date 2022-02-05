#!/bin/python3
'''
https://www.hackerrank.com/challenges/find-the-running-median/problem

  

'''

# from heapq import heappush, heappop
import heapq
import os
import sys

from collections import deque

class Node():
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.parent = None
    self.left = None
    self.right = None
    self.left_count = 0
    self.right_count = 0
  
  def __str__(self):
    return "{}: {}".format(self.key, self.value)

class AVLTree():
  def __init__(self):
    self.root:Node = None
    
  def __str__(self):
    s = ''
    q = deque()
    q.append(self.root)
    while q:
      node = q.popleft()

      s += '({},{}): left: {}, right: {}\n'.format(node.key, node.value, 
      node.left.key if node.left else '', 
      node.right.key if node.right else '')
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
      
    return s

  def inorder(self, n=None):
    if n is None:
      n = self.root

    result_arr = []
    if n.left:
      result_arr += self.inorder(n.left)
    result_arr.append((n.key, n.value))
    if n.right:
      result_arr += self.inorder(n.right)
    
    return result_arr

  def size(self):
    return self.root.left_count + self.root.right_count + 1

  # single rotaion Left-Left
  def llrotate(self, prev_root):
    new_root = prev_root.left
    new_root.parent = prev_root.parent
    
    if prev_root.parent:
      if prev_root.parent.left is prev_root:
        prev_root.parent.left = new_root
      else:
        prev_root.parent.right = new_root
    else:
      self.root = new_root

    prev_root.parent = new_root
    prev_root.left = new_root.right
    prev_root.left_count = prev_root.left.left_count + prev_root.left.right_count + 1 if prev_root.left else 1
    new_root.right = prev_root
    
    new_root.right_count = new_root.right.left_count + new_root.right.right_count + 1
    prev_root.left_count = 0
  
  # single rotation Right-right
  def rrrotate(self, prev_root):
    new_root = prev_root.right
    new_root.parent = prev_root.parent

    if prev_root.parent:
      if prev_root.parent.right is prev_root:
        prev_root.parent.right = new_root
      else:
        prev_root.parent.left = new_root
    else:
      self.root = new_root

    prev_root.parent = new_root
    prev_root.right = new_root.left
    prev_root.right_count = prev_root.right.left_count + prev_root.right.right_count + 1 if prev_root.right else 1
    new_root.left = prev_root
    
    new_root.left_count = new_root.left.left_count + new_root.left.right_count + 1
    prev_root.right_count = 0

  # double rotation Left-Right
  def lrrotate(self, prev_root):
    new_root = prev_root.left.right
    inte_node = prev_root.left

    new_root.right = prev_root
    new_root.left = prev_root.left
    new_root.parent = prev_root.parent

    if prev_root.parent:
      if prev_root.parent.left is prev_root:
        prev_root.parent.left = new_root
      else:
        prev_root.parent.right = new_root
    else:
      self.root = new_root

    prev_root.parent = new_root
    prev_root.left = None
    prev_root.left_count = 0

    inte_node.parent = new_root
    inte_node.right = None
    inte_node.right_count = 0

    new_root.left_count = new_root.left.left_count + new_root.left.right_count + 1
    new_root.right_count = new_root.right.left_count + new_root.right.right_count + 1

  # double rotation Right-Left
  def rlrotate(self, prev_root):
    new_root = prev_root.right.left
    inte_node = prev_root.right

    new_root.left = prev_root
    new_root.right = prev_root.right
    new_root.parent = prev_root.parent

    if prev_root.parent:
      if prev_root.parent.left is prev_root:
        prev_root.parent.left = new_root
      else:
        prev_root.parent.right = new_root
    else:
      self.root = new_root

    prev_root.parent = new_root
    prev_root.right = None
    prev_root.right_count = 0

    inte_node.parent = new_root
    inte_node.left = None
    inte_node.left_count = 0

    new_root.left_count = new_root.left.left_count + new_root.left.right_count + 1
    new_root.right_count = new_root.right.left_count + new_root.right.right_count + 1
    
  # check the balance from newly added node
  def balance(self, node):
    c = node
    p = c.parent
    pp = p.parent

    while p is not None and pp is not None:
      if pp.left_count > pp.right_count + 1:
        if c.key < p.key:  
          self.llrotate(pp)    # Left-Left rotation
        else: 
          self.lrrotate(pp)   # Left-Right rotation
        break
      elif pp.right_count > pp.left_count + 1:
        if c.key > p.key: 
          self.rrrotate(pp)    # Right-Right rotation
        else: 
          self.rlrotate(pp)   # Right-Left rotation
        break
      c = c.parent
      p = p.parent
      pp = pp.parent


  # update child count
  def update_child_count(self, node):
    p = node.parent
    child = node
    while p is not None:
      if p.left is child:
        p.left_count = child.left_count + child.right_count + 1
      else:
        p.right_count = child.left_count + child.right_count + 1
      child = p
      p = p.parent

  # insert
  def insert(self, key, value):
    parent = self.root
    node = None
    if parent == None:
      node = Node(key, value)
      self.root = node
      return node
    else:
      while True:
        if key < parent.key:
          if parent.left == None:
            node = Node(key, value)
            node.parent = parent
            parent.left = node

            self.update_child_count(node)
            break

          else:
            parent = parent.left
        elif key > parent.key:
          if parent.right == None:
            node = Node(key, value)
            node.parent = parent
            parent.right = node

            self.update_child_count(node)
            break
          else:
            parent = parent.right
        else: # dulpicated key
          raise("duplicated key: {}".format(key))

      # end of while
      self.balance(node)
      return node
    

  def find(self, key) -> Node:
    node:Node = self.root
    while node.key != key:
      if node.key <= key:
        node = node.left
      else:
        node = node.right

    if node.key == key:
      return node
    else:
      return None

  def delete(self, key):
    pass



#
# Complete the runningMedian function below.
#
# a is array of number
def runningMedian(a):
  result = []
  tree = AVLTree()
  
  for n in a:
    tree.insert(n,n)
       
    arr = tree.inorder()
    l = len(arr) 
    m = (arr[int(l/2)-1][0] + arr[int(l/2)][0]) / 2 if l%2 == 0 else arr[int(l/2)][0]
    
    result.append(m)

  return result

if __name__ == '__main__':
  testcases = [
    ([12,4,5,3,8,7],  [12,8,5,4.5,5,6]), 
    ([1,2,3,4,5,6,7,8,9,10], [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5])
  ]
  
  for i, case in enumerate(testcases):
    expected_output = case[1]
    output = runningMedian(case[0])
    print("test case {} is {}".format(i, "correct" if expected_output == output else "incorrect"))
    if expected_output != output:
      print("  expected result: {}".format(expected_output))
      print("  actual result: {}".format(output))

