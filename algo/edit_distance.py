'''

This implements the calculation of edit distance of two given strings

for detail of edit distance, please refer: https://en.wikipedia.org/wiki/Levenshtein_distance


'''

import sys

def edit_distance(s1, s2):
  w = len(s1) + 1
  h = len(s2) + 1
  
  edit_dist_table = [[0 for i in range(w)] for j in range(h)]

  # init first row
  for i in range(w):
    edit_dist_table[0][i] = i

  # init first column
  for j in range(h):
    edit_dist_table[j][0] = j

  for j in range(1, w, 1):
    for i in range(1, h, 1):
      sub_cost = 0 if s1[j-1] == s2[i-1] else 1
      edit_dist_table[i][j] = min(
        edit_dist_table[i-1][j] + 1,                # deletion cost
        edit_dist_table[i][j-1] + 1,                # insert cose
        edit_dist_table[i-1][j-1] + sub_cost)       # substitution cose
      
  return edit_dist_table[h-1][w-1]

if __name__ == '__main__':
  testcases = [
    ("abc", "abc", 0),
    ("abc", "acc", 1),
    ("kitten", "sitting", 3),
    ("saturday", "sunday", 3),
  ]
  
  for i, case in enumerate(testcases):
    expected_output = case[2]
    output = edit_distance(case[0], case[1])
    print("test case {} is {}".format(i, "correct" if expected_output == output else "incorrect"))
