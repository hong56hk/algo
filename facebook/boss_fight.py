from typing import List
# Write any import statements here

def getMaxDamageDealt_bf(N: int, H: List[int], D: List[int], B: int) -> float:
  max_dmg = 0

  for i in range(N):
    for j in range(i+1,N):
      total_dmg_1 = H[i] * D[i] + (H[i] + H[j]) * D[j]
      total_dmg_2 = H[j] * D[j] + (H[i] + H[j]) * D[i]
      max_dmg = max(max_dmg, total_dmg_1, total_dmg_2)

  return max_dmg / B

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  best_i = 0
  best_j = 0
  
  max_dmg = 0

  # find the best attacker
  for wi in range(N):
    dmg = H[wi] * D[wi]
    if dmg > max_dmg: # stand at the back
      max_dmg = dmg
      best_j = wi

  for wi in range(N):
    dmg = H[wi] * D[wi] + (H[wi] + H[best_j]) * D[best_j]
    if dmg > max_dmg and wi != best_j:
      best_i = wi
  
  
  print("best i:{} j:{}".format(best_i, best_j))
  total_dmg = (H[best_i] * D[best_i] + (H[best_i] + H[best_j]) * D[best_j]) / B
  return total_dmg

if __name__ == "__main__":
  print(getMaxDamageDealt(3, [2,1,4], [3,1,2], 4))
  print(getMaxDamageDealt(4, [1,1,2,100], [1,2,1,3], 8))
  print(getMaxDamageDealt(4, [1,1,2,3], [1,2,1,100], 8))
