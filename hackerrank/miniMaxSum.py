'''
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    print(sum(arr_sorted[:4]), sum(arr_sorted[len(arr_sorted)-4:]))

if __name__ == '__main__':
    arr = list([1,5,3,4,2])
    miniMaxSum(arr)
