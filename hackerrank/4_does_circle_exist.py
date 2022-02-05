#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

def doesCircleExist(commands):
    # Write your code here
    result = []
    
    for cmd_list in commands:
        cur_pos = (0, 0) # (x, y)
        cur_ori = 0 # in degree
        moved = False
        for cmd in cmd_list*4:
            if cmd == "G":
                moved = True
                if cur_ori%360 == 0: 
                    cur_pos = (cur_pos[0], cur_pos[1] + 1)
                elif cur_ori%360 == 90:
                    cur_pos = (cur_pos[0] + 1, cur_pos[1])

                elif cur_ori%360 == 180:
                    cur_pos = (cur_pos[0], cur_pos[1] - 1)

                elif cur_ori%360 == 270:
                    cur_pos = (cur_pos[0] - 1, cur_pos[1])
            elif cmd == "L":
                cur_ori -= 90
                
            elif cmd == "R":
                cur_ori += 90
            
            else:
                result.append("NO")
                break
            # can add early exit or do some transformation to check
        result.append("YES" if cur_pos == (0,0) and (( moved and cur_ori%360 == 0 ) or not moved ) else "NO")
    return result



if __name__ == '__main__':
    print(doesCircleExist([

        "GGGGR",
        "RGL",
        "GGGGGGR",
        "RGL",
        "",             # yes
        "LLGLLG",       # yes
        "LGLLGL",       # yes
        "L",            # YES
        "RGRGRGRGR",    # NO
        "GLLG",         # NO
        "GLLGLL",       # YES
        "GRGL",         # no
        "RGRGRGRG"      # yes
    ]))
    