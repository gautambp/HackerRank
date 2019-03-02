# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/jesse-and-cookies/problem
#!/bin/python3

import os
import sys
import heapq

#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    cnt = 0
    while len(A) > 0:
        #print(A)
        if A[0] < k:
            n1 = heapq.heappop(A)
            if len(A) == 0:
                return -1
            n2 = heapq.heappop(A)
            c = n1 + 2*n2
            heapq.heappush(A, c)
            cnt += 1
        else:
            return cnt
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
