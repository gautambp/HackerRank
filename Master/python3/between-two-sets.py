# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/between-two-sets/problem
#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    min_no = 999999999;
    max_no = 0;
    total_x = 0;
    range_a = range(len(a))
    range_b = range(len(b))
    for i in range_a:
        if a[i] < min_no:
            min_no = a[i]
        if a[i] > max_no:
            max_no = a[i]
    for j in range_b:
        if b[j] < min_no:
            min_no = b[j]
        if b[j] > max_no:
            max_no = b[j]
    if min_no < 1:
        min_no = 1
    for no in range(min_no, max_no+1):
        match_a = True
        for i in range_a:
            if no % a[i] != 0:
                match_a = False
                break
        if match_a:
            match_b = True
            for j in range_b:
                if b[j] % no != 0:
                    match_b = False
            if match_b:
                total_x = total_x + 1
    return total_x


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
