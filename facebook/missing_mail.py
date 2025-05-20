from typing import List
# Write any import statements here
import math

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
  sum = 0
  value_in_room = 0
  
  for i in range(N-1):
    v = V[i]
    v1 = V[i+1]
    today_value = value_in_room + v
    tmr_expected_value = today_value * (1-S)
    
    n = 0
    if S == 1:
      n = 0 # take out immediately
    elif S == 0:
      n = N + 1  # just take out at the end
    else:
      n = math.log(C/today_value) / math.log(S)
    
    if (today_value > C) and (0 < n < 1) :
      sum += today_value - C
      value_in_room = 0
      print("taken on day {}".format(i+1))
    else:  
      value_in_room = tmr_expected_value
  
  # last day
  last_day_value = V[-1]
  if value_in_room + last_day_value > C:
    print("taken on day {}".format(N))
    sum += value_in_room + last_day_value - C
  
  return sum



if __name__ == "__main__":
  # print(getMaxExpectedProfit(5, [10,2,8,6,4], 5, 0.0))
  # print(getMaxExpectedProfit(5, [10,2,8,6,4], 5, 1.0))
  # print(getMaxExpectedProfit(5, [10,2,8,6,4], 3, 0.5))
  print(getMaxExpectedProfit(5, [10,2,8,6,4], 3, 0.15))