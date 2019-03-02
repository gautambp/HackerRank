# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the plusMinus function below.
def plusMinus(arr):
    arr_len = len(arr);
    p_sum = 0;
    n_sum = 0;
    z_sum = 0;
    for val in arr:
        if val > 0:
            p_sum = p_sum + 1;
        elif val < 0:
            n_sum = n_sum + 1;
        else:
            z_sum = z_sum + 1;
    print('%(number)#f' % {'number': p_sum/arr_len});
    print('%(number)#f' % {'number': n_sum/arr_len});
    print('%(number)#f' % {'number': z_sum/arr_len});


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
