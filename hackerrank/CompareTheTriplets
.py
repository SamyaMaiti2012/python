'''
https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    a_res = 0
    b_res = 0
    for a_dash,b_dash in zip(a, b) :
        if a_dash > b_dash :
            a_res += 1
        elif a_dash < b_dash :
            b_res += 1
    return [a_res, b_res]


if __name__ == '__main__':
    a = list([1,2,3])
    b = list([1,2,3])

    result = solve(a, b)
    print(result)
