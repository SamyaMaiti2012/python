'''
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''

import math
import os
import random
import re
import sys
import collections

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar_max = max(ar)
    ctr = collections.Counter(ar)
    return ctr[ar_max]

if __name__ == '__main__':
    ar = list([3,2,1,3,4,5,4,4,4,4,4])
    result = birthdayCakeCandles(ar)
    print(result)
