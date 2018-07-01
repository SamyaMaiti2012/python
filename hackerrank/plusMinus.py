'''
https://www.hackerrank.com/challenges/plus-minus/problem
'''


import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    posative_count = sum(arr_element > 0 for arr_element in arr)
    negative_count = sum(arr_element < 0 for arr_element in arr)
    zero_count = sum(arr_element == 0 for arr_element in arr)

    print(posative_count/n)
    print(negative_count/n)
    print(zero_count/n)

if __name__ == '__main__':
    n = 6
    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
