#!/bin/python3
'''
An implementation of AVL tree

 - An AVL (Adelson-Velskii and Landis) tree is a binary search tree with a
   balance condition.

 - An AVL tree is identical to a binary search tree,
   except that for every node in the tree, the height of the left and right
   subtrees can differ by at most 1.

 - With an AVL tree, all the tree operations can be performed in O(log n) time,
   except insertion.


'''

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
    s = 'root: {}\n'.format(self.root.key)
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
    while True:
      if node.key < key:
        node = node.left
      elif node.key > key:
        node = node.right
      else:
        return node

  def left_most(self) -> Node:
    node = self.root
    while node.left:
      node = node.left
    return node

  def right_most(self) -> Node:
    node = self.root
    while node.right:
      node = node.right
    return node

  def delete(self, key, root=None):
    if root is None:
      return root

    if key < root.key:
      root.left = self.delete(key, root.left)
    elif key > root.key:
      root.right = self.delete(key, root.right)
    else:
      if root.left is None or root.right is None:
        temp = root.left if root.left else root.right
        # no child
        if temp is None:
          root = None
        else:
          root = temp
      else:
        temp = self.left_most(root.right)
        root.key = temp.key
        root.right = self.delete(temp.key, root.right)

    # if the tree had only one node
    if root is None:
      return root

    # update the height of the current node
    root.left_count = root.left.left_count + 1
    root.right_count = root.right.right_count + 1

    self.balance(root)
    return root




if __name__ == '__main__':
  print("started")
  t = AVLTree()
  t.insert("b", "boy")
  t.insert("a", "apple")
  t.insert("c", "cat")
  print(t)

  print("--- 1. test for left-left rotation")
  t = AVLTree()
  t.insert(5, 5)
  t.insert(4, 4)
  t.insert(3, 3)
  print(t)

  print("--- 2. test for right-right rotation")
  t = AVLTree()
  t.insert(1, None)
  t.insert(2, None)
  t.insert(3, None)
  t.insert(4, None)
  t.insert(5, None)
  t.insert(6, None)
  t.insert(7, None)
  t.insert(8, None)
  t.insert(9, None)
  t.insert(10, None)
  inorder = t.inorder()
  print(inorder)

  print("--- 3. test for right-left rotation")
  t = AVLTree()
  t.insert(5, 5)
  t.insert(7, 7)
  t.insert(6, 6)
  print(t)

  print("--- 4. test for left-right rotation")
  t = AVLTree()
  t.insert(5, 5)
  t.insert(3, 3)
  t.insert(4, 4)
  print(t)

  print("--- 5. test for left-right rotation")
  t = AVLTree()
  t.insert(7, None)
  t.insert(4, None)
  t.insert(14, None)
  t.insert(2, None)
  t.insert(6, None)
  t.insert(13, None)
  t.insert(15, None)
  t.insert(1, None)
  t.insert(3, None)
  t.insert(5, None)
  t.insert(12, None)
  print(t)
  t.insert(11, None)
  print(t)


  print("--- 6. test")
  t = AVLTree()
  t.insert(12, None)
  t.insert(4, None)
  t.insert(5, None)
  print(t)
  t.insert(3, None)
  t.insert(8, None)
  print(t)
  t.insert(7, None)
  print(t)

  print("--- 7. test delete")
  t = AVLTree()
  t.insert(10, None)
  t.insert(9, None)
  t.insert(2, None)
  t.insert(3, None)
  print(t)
  t.insert(4, None)
  print(t)
  t.insert(5, None)
  print(t)
  t.insert(8, None)
  print(t)
  t.insert(7, None)
  print(t)
  t.insert(6, None)
  print(t)

