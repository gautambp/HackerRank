# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/company-logo/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    c = Counter(sorted(s))
    for k in c.most_common(3):
        print('{} {}'.format(k[0], k[1]))

