#!/bin/python3

import math
import os


def calculateMinimumHP(dungeon) -> int:
  h = len(dungeon)
  w = len(dungeon[0])
  best_hp_map = [[None for i in range(w)] for j in range(h)]
  min_hp_map = [[None for i in range(w)] for j in range(h)] 
  
  path_dict = {}
  path_dict[best_hp_map[0][0]] = [[(0,0)]]
  min = 0

  for i in range(h): # row
    for j in range(w): # col
      if i-1 >= 0 and j-1 >= 0:
        best_hp_map[i][j] = max( best_hp_map[i-1][j], best_hp_map[i][j-1]) + dungeon[i][j]
      
      elif i-1 >= 0:
        best_hp_map[i][j] = best_hp_map[i-1][j] + dungeon[i][j]
      
      elif j-1 >= 0:
        best_hp_map[i][j] = best_hp_map[i][j-1] + dungeon[i][j]
      
      else: # start
        best_hp_map[i][j] = dungeon[i][j]
        
  print(best_hp_map)
  
  


  return min

if __name__ == '__main__':
  map = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
  ]
  print(calculateMinimumHP(map))