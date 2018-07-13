'''
https://www.hackerrank.com/challenges/apple-and-orange/problem
'''

import math
import os
import random
import re
import sys
import collections


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount=0
    for i in apples:
        if s<=a+i<=t:
            acount+=1

    ocount=0
    for i in oranges:
        if s<=b+i<=t:
            ocount+=1
    print(acount)
    print(ocount)

if __name__ == '__main__':
    s = 37455
    t = 87275
    a = 35609
    b = 89610
    m = 1
    n = 1

    apples = list([19736,19374,-68796,0,-68800,-80005,-88])
    oranges = list([383,-8147,73241,-33256,2022])

    countApplesAndOranges(s, t, a, b, apples, oranges)
