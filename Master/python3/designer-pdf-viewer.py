# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    a_idx = ord('a')
    max_h = 0
    for w in word:
        h1 = h[ord(w)-a_idx]
        if h1 > max_h:
            max_h = h1
    return max_h * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
