#!/bin/python3

import math
import os


def calculateMinimumHP(dungeon) -> int:
  h = len(dungeon)
  w = len(dungeon[0])
  min_hp_map = [[None for i in range(w)] for j in range(h)]
  
  path_dict = {}
  path_dict[min_hp_map[0][0]] = [[(0,0)]]
  min = 0

  for i in range(h): # row
    for j in range(w): # col
      if i-1 >= 0 and j-1 >= 0:
        min_hp_map[i][j] = max( min_hp_map[i-1][j], min_hp_map[i][j-1]) + dungeon[i][j]
      
      elif i-1 >= 0:
        min_hp_map[i][j] = min_hp_map[i-1][j] + dungeon[i][j]
      
      elif j-1 >= 0:
        min_hp_map[i][j] = min_hp_map[i][j-1] + dungeon[i][j]
      
      else: # start
        min_hp_map[i][j] = dungeon[i][j]
  print(min_hp_map)
  
  cur_pos = (0,0)
  while cur_pos != (h, w)
    min_hp = min_hp_map[cur_pos[0]][cur_pos[1]]
    if min_hp not in path_dict.keys():
      path_dict[min_hp] = [[cur_pos]]
    else:
      for path in path_dict[min_hp]
        last_pos = path[-1]
        if last_pos[0] == cur_pos[0] -1 or last_pos[1] == cur_pos[1] - 1:  # adj grid
          path.append(cur_pos)

  return min

if __name__ == '__main__':
  map = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
  ]
  print(calculateMinimumHP(map))