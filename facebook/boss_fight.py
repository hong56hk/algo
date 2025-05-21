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
  best_warrier = -1
  second_warrier = -1
  
  max_dmg = 0
  second_dmg = 0

  # find the best attacker
  for wi in range(N):
    dmg = H[wi] * D[wi]
    if dmg >= max_dmg: # stand at the back
      second_warrier = best_warrier
      second_dmg = max_dmg

      best_warrier = wi
      max_dmg = dmg

    if second_warrier == -1 and wi != best_warrier and dmg > second_dmg:  
      second_warrier = wi
      second_dmg = dmg

  total_dmg_1 = H[best_warrier] * D[best_warrier] + (H[best_warrier] + H[second_warrier]) * D[second_warrier]
  total_dmg_2 = H[second_warrier] * D[second_warrier] + (H[best_warrier] + H[second_warrier]) * D[best_warrier]
  
  total_dmg = max(total_dmg_1, total_dmg_2) / B
  return total_dmg

if __name__ == "__main__":
  # print(getMaxDamageDealt(3, [2,1,4], [3,1,2], 4))
  print(getMaxDamageDealt(4,    [1,1,2,100], [1,2,1,3], 8))
  print(getMaxDamageDealt_bf(4, [1,1,2,100], [1,2,1,3], 8))

  print(getMaxDamageDealt(4, [1,1,2,3], [1,2,1,100], 8))
  print(getMaxDamageDealt_bf(4, [1,1,2,3], [1,2,1,100], 8))
