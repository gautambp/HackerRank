# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-32-pandigital-products/problem
from itertools import permutations

def getMatchedProduct(l):
    len_l = len(l)
    if len_l == 3:
        if l[0]*l[1] == l[2]:
            return l[2]
    elif len_l == 4:
        ans = l[2]*10+l[3]
        if l[0]*l[1] == ans:
            return ans
    elif len_l == 5:
        ans = l[3]*10+l[4]
        if l[0]*(l[1]*10+l[2]) == ans:
            return ans
        if (l[0]*10+l[1])*l[2] == ans:
            return ans
    elif len_l == 6:
        ans = l[3]*100+l[4]*10+l[5]
        if l[0]*(l[1]*10+l[2]) == ans:
            return ans
        if (l[0]*10+l[1])*l[2] == ans:
            return ans
    elif len_l == 7:
        ans = l[4]*100+l[5]*10+l[6]
        if l[0]*(l[1]*100+l[2]*10+l[3]) == ans:
            return ans
        if (l[0]*10+l[1])*(l[2]*10+l[3]) == ans:
            return ans
        if (l[0]*100+l[1]*10+l[2])*l[3] == ans:
            return ans
    elif len_l == 8:
        ans = l[4]*1000+l[5]*100+l[6]*10+l[7]
        if l[0]*(l[1]*100+l[2]*10+l[3]) == ans:
            return ans
        if (l[0]*10+l[1])*(l[2]*10+l[3]) == ans:
            return ans
        if (l[0]*100+l[1]*10+l[2])*l[3] == ans:
            return ans
    elif len_l == 9:
        ans = l[5]*1000+l[6]*100+l[7]*10+l[8]
        if l[0]*(l[1]*1000+l[2]*100+l[3]*10+l[4]) == ans:
            return ans
        if (l[0]*10+l[1])*(l[2]*100+l[3]*10+l[4]) == ans:
            return ans
        if (l[0]*100+l[1]*10+l[2])*(l[3]*10+l[4]) == ans:
            return ans
        if (l[0]*1000+l[1]*100+l[2]*10+l[3])*l[4] == ans:
            return ans
    return -1

n = int(input())
l = [i for i in range(1, n+1)]
product_l = set()
for i in permutations(l, n):
    ans = getMatchedProduct(i)
    if ans > 0:
        product_l.add(ans)
print(sum(product_l))
