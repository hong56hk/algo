#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minFolders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER cssFiles
#  2. INTEGER jsFiles
#  3. INTEGER readMeFiles
#  4. INTEGER capacity
#

def minFolders(cssFiles, jsFiles, readMeFiles, capacity):
    # Write your code here
    folder_c = 0
    re_readme = readMeFiles
    re_ccs = cssFiles
    re_js = jsFiles
    
    while re_readme > 0 or re_ccs > 0 or re_js > 0:
        folder_c += 1
        folder_space = capacity
        if re_readme > 0:
            re_readme -= 1
            folder_space -= 1

        if folder_space%2 == 0:
            if re_ccs >= folder_space/2 and re_js >= folder_space/2:
                re_ccs -= folder_space/2
                re_js -= folder_space/2

            elif re_ccs >= folder_space/2:
                re_ccs -= (re_js+1)
                re_js -= re_js

            elif re_js >= folder_space/2:
                re_ccs -= re_ccs
                re_js -= (re_ccs+1)
            
            else:
                re_ccs -= re_ccs
                re_js -= re_js
            
        else:
            upper_count = math.ceil(folder_space/2)
            lower_count = upper_count - 1
            if re_ccs > re_js:
                if re_ccs >= upper_count and re_js >= lower_count:
                    re_ccs -= upper_count
                    re_js -= lower_count

                elif re_ccs >= upper_count:
                    re_ccs -= re_js+1
                    re_js -= re_js

                elif re_js >= lower_count:
                    re_ccs -= re_ccs+1
                    re_js -= re_ccs
                
                else:
                    re_css -= re_css
                    re_js -= re_js

            else:
                if re_ccs >= lower_count and re_js >= upper_count:
                    re_ccs -= lower_count
                    re_js -= upper_count

                elif re_ccs >= lower_count:
                    re_ccs -= re_js+1
                    re_js -= re_js

                elif re_js >= upper_count:
                    re_ccs -= re_ccs+1
                    re_js -= re_ccs
                    
                else:
                    re_css -= re_css
                    re_js -= re_js

    return folder_c
        



if __name__ == '__main__':
    print(minFolders(0, 13, 7, 5))