'''
https://www.hackerrank.com/challenges/grading/problem
'''

import os
import sys
import math

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    grade_altered =[]
    for grade in grades:
        if grade >= 38:
            up_nearest_mul_five = math.ceil(grade/5)*5
            if (up_nearest_mul_five - grade < 3) :
                grade_altered.append(up_nearest_mul_five)
            else:
                grade_altered.append(grade)
        else:
            grade_altered.append(grade)
    return grade_altered


if __name__ == '__main__':

    grades = [73,67,38,33]
    result = gradingStudents(grades)
    print(result)
