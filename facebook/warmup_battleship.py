from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  ship_count = 0
  for r in range(R):
    for c in range(C):
      if G[r][c] == 1:
        ship_count += 1
        
  return ship_count/(R*C)
