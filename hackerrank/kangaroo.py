'''
https://www.hackerrank.com/challenges/kangaroo/problem
'''

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    is_merge = ""
    if(x1 < x2 and v1 > v2) :
        diff_start = x2-x1
        diff_jump = v1-v2
        req_jumps = diff_start/diff_jump
        if (req_jumps.is_integer()) :
            is_merge="YES"
        else:
            is_merge="NO"
    elif(x1 > x2 and v2 > v1) :
        diff_start = x1-x2
        diff_jump = v2-v1
        req_jumps = diff_start/diff_jump
        if (req_jumps.is_integer()) :
            is_merge="YES"
        else:
            is_merge="NO"
    elif(x1 == x2 and v2 == v1) :
        is_merge="YES"
    else:
        is_merge="NO"
    return is_merge


if __name__ == '__main__':
    x1 = 6
    v1 = 1
    x2 = 5
    v2 = 6
    result = kangaroo(x1, v1, x2, v2)
    print(result)
