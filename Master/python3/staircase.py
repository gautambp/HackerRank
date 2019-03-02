# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/staircase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    p_str = '';
    for i in range(n):
        p_str = p_str + '#';
        print(p_str.rjust(n));
            

if __name__ == '__main__':
    n = int(input())

    staircase(n)
