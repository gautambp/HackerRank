# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/matrix-script/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product 


nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ''
for i in range(m):
    for j in range(n):
        s += matrix[j][i]
#print(s)
val = re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s)
print(val.strip())

