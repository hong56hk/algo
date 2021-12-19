"""
find the average of a given binary tree on each level

"""
from queue import Queue


class Node:
  def __init__(self, v) -> None:
    self.val = v
    self.left:Node = None
    self.right:Node = None

root = Node(4)
root.left = Node(7)
root.right = Node(9)

root.left.left = Node(10)
root.left.right = Node(2)

root.left.right.right = Node(6)
root.left.right.right.left = Node(2)

root.right.right = Node(6)


def average_value(node_root:Node):
  count_dict = {}
  q = Queue()
  q.put({
    "n": node_root,
    "lvl": 0
  })
  
  while q.qsize() > 0:
    child = q.get()
    lvl = child['lvl']
    node = child['n']
    if lvl not in count_dict.keys():
      count_dict[lvl] = [node.val]
    else:
      count_dict[lvl].append(node.val)

    if node.left:
      q.put({
        "n": node.left,
        "lvl": lvl + 1
      })
    if node.right:
      q.put({
        "n": node.right,
        "lvl": lvl + 1
      })
  
  print(count_dict)

average_value(root)