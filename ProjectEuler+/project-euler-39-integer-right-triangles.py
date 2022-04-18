# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-39-integer-right-triangles/problem
import math

mn_ub = 1201
p_ub = 5000000
pl = [0]*(p_ub+1)
ans = [0]*(p_ub+1)
def init():
    for m in range(2, mn_ub):
        for n in range(1, m):
            if (m+n) % 2 != 0 and math.gcd(m,n) == 1:
                p = 2 * m * (m + n)
                k = 1
                while k*p <= p_ub:
                    pl[k*p] += 1
                    k += 1
    for i in range(1, p_ub+1):
        if pl[i] > pl[ans[i-1]]:
            ans[i] = i
        else:
            ans[i] = ans[i-1]

init()
for _ in range(int(input())):
    n = int(input())
    print(ans[n])
