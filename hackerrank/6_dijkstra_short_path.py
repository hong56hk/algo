#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

# Complete the shortestReach function below.


class Node():
    def __init__(self, id):
        self.id = id
        self.adj_node_list = []  # (adjacent node, length)

# shortestReach has the following parameter(s):
# n: the number of nodes in the graph
# edges: a 2D array of integers where each  consists of three integers that represent the start and end nodes of an edge, followed by its length
# s: the start node number

def shortestReach(n, edges, s):
    s -= 1
    short_path_arr = [-1 for _ in range(n)]
    short_path_arr[s] = 0
    q = deque()

    node_dict = {}
    for (start, end, weight) in edges:
        start -= 1
        end -= 1

        start_node = None
        if start not in node_dict.keys():
            start_node = Node(start)
            node_dict[start] = start_node
        else:
            start_node = node_dict[start]
        end_node = None
        if end not in node_dict.keys():
            end_node = Node(end)
            node_dict[end] = end_node
        else:
            end_node = node_dict[end]

        start_node.adj_node_list.append((end_node, weight))
        end_node.adj_node_list.append((start_node, weight))
    
    q.append(node_dict[s])
    while len(q) > 0:
        n = node_dict[q.pop().id]
        for (adj_node, weight) in n.adj_node_list:
            if short_path_arr[adj_node.id] == -1 or short_path_arr[adj_node.id] >= weight + short_path_arr[n.id]
                short_path_arr[adj_node.id] = weight + short_path_arr[n.id]
            if adj_node.id != n.id and short_path_arr[adj_node.id] != -1:
                q.append(adj_node)

    return short_path_arr

if __name__ == '__main__':
    n = 4
    edges = [
        (1, 2, 24),
        (1, 4, 20),
        (3, 1, 3),
        (4, 3, 12),
    ]
    s = 1
    print(shortestReach(n, edges, s))
