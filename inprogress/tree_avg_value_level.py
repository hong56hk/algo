"""
find the average of a given binary tree on each level

    4
   / \
  7   9
 / \   \
10  2   6
     \
      6
       \
        2
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


def bfs(node_root:Node):
  data = {}
  q = Queue()
  q.put({
    "n": node_root,
    "lvl": 0
  })
  
  while q.qsize() > 0:
    child = q.get()
    lvl = child['lvl']
    node = child['n']
    if lvl not in data.keys():
      data[lvl] = [node.val]
    else:
      data[lvl].append(node.val)

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

  print(data)

def dfs(node_root:Node):
  data = []
  s = []
  s.append(node_root)

  while len(s) > 0:
    node = s.pop()
    data.append(node.val)

    if node.right:
      s.append(node.right)
    if node.left:
      s.append(node.left)
  print(data)      

bfs(root)
dfs(root)