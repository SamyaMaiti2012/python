import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diagonal_lr = sum(arr[i][i] for i in range(n))
    diagonal_rl = sum(arr[i][n-i-1] for i in range(n))
    return abs(diagonal_lr - diagonal_rl)

if __name__ == '__main__':
    n = 3
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    result = diagonalDifference(arr)
    print(result)
