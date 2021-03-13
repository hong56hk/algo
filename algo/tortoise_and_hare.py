'''

This implements simple tortoise and hare algorithm which is a cycle detection algorithm

input:
number of nodes
<source node id> <destination ndoe id>
<source node id> <destination ndoe id>
...


'''

import sys

class Node:
  def __init__(self, pos):
    self.cur_pos = pos
    self.next_node = None

def find_cyclic(start_node):
  tortoise = start_node
  hare = start_node
  while tortoise.next_node and hare.next_node.next_node:
    tortoise = tortoise.next_node
    hare = hare.next_node.next_node

    if tortoise.cur_pos == hare.cur_pos:
      tortoise = start_node
      while tortoise.cur_pos != hare.cur_pos:
        tortoise = tortoise.next_node
        hare = hare.next_node

      return tortoise
  return False

node_count = int(input())
node_list = [Node(i) for i in range(node_count)]

for _ in range(node_count):
  line = input()
  line_arr = line.strip().split(" ")
  src = int(line_arr[0])
  dest = int(line_arr[1])
  node_list[src].next_node = node_list[dest]


# debug
node = node_list[0]
print("{} -> {}".format(node.cur_pos, node.next_node.cur_pos))
count = 0
while node.next_node and count < len(line):
  node = node.next_node
  print("{} -> {}".format(node.cur_pos, node.next_node.cur_pos))
  count+=1
  
meetup = find_cyclic(node_list[0])
print("meet up: {}".format(meetup.cur_pos))
          
