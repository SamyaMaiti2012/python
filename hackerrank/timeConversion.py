'''
https://www.hackerrank.com/challenges/time-conversion/problem
'''

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s_t = datetime.strptime(s, '%I:%M:%S%p')
    return s_t.strftime('%H:%M:%S')

if __name__ == '__main__':
    result = timeConversion('07:05:45PM')
    print(result)
