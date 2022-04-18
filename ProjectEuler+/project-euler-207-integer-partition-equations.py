# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-207-integer-partition-equations/problem
import math

P = [None, None, (1, 1, 2), (1, 1, 2), (1, 1, 2), (1, 1, 2)]
l2 = math.log(2)

def is_partition(n):
    n1 = (1 + 4*n) ** 0.5
    if (n1 - int(n1)) == 0:
        t = math.log((1+n1)/2)/l2
        return (True, ((t-int(t)) == 0))
    return (False, False)

def find_low_m(a, b):
    i_cnt, r_cnt, low_p = P[-1]
    if i_cnt/r_cnt > a/b:
        k = len(P)
        while True:
            r, i = is_partition(k)
            if r: 
                r_cnt += 1
                if i: 
                    i_cnt += 1
            last_p = P[-1]
            if i_cnt/r_cnt < last_p[0]/last_p[1]:
                low_p = k
            P.append((i_cnt, r_cnt, low_p))
            if i_cnt/r_cnt < a/b:
                return k
            k += 1
    else:
        k = len(P)-1
        last_low_p = low_p
        while k>=1:
            i_cnt, r_cnt, low_p = P[k]
            if i_cnt/r_cnt > a/b:
                return last_low_p
            last_low_p = low_p
            k -= 1

for _ in range(int(input())):
    s = input().split()
    a, b = int(s[0]), int(s[1])
    print(find_low_m(a,b))
