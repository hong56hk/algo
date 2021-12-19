
class Node:
  def __init__(self, value:int) -> None:
    self.value = value
    # self.prev:Node = None
    self.next:Node = None

  

def move_zeros_to_left(A):
  root:Node = None
  last:Node = None
  for a in A:
    if root == None:
      root = Node(a)
      last = root
    else:
      node = Node(a)
      if a == 0:
        node.next = root
        root = node
      else:
        last.next = node
        last = node
  
  arr = []
  curr = root
  while curr != None:
    arr.append(curr.value)
    curr = curr.next

  return arr

def move_zeros_to_left_2(A):
  arr = []
  for a in A:
    if a == 0:
      arr.insert(0, a)
    else:
      arr.append(a)
  return arr


l = [1,2,4,0,6,0,663,4,60,0]
print(move_zeros_to_left_2(l))