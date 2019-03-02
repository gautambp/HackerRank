# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/grading-students/problem
#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    final_grades = [];
    for g in grades:
        round_g = 5*(int(g/5)+1);
        if g >= 38 and round_g - g < 3:
            final_grades.append(round_g);
        else:
            final_grades.append(g);
    return final_grades;

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
