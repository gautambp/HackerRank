# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/mini-max-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sum = 0;
    min_val = arr[0];
    max_val = arr[0];
    for val in arr:
        if val < min_val:
            min_val = val;
        if val > max_val:
            max_val = val;
        arr_sum = arr_sum + val;
    print('%(min_sum)#d %(max_sum)#d' % {'min_sum':arr_sum-max_val, 'max_sum':arr_sum-min_val});

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
