# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-12-highly-divisible-triangular-number/problem
ub = 21750
inc = [4, 2, 4, 2, 4, 6, 2, 6]

def getPrimeFactorCount(n, p):
    cnt = 0
    while n%p == 0:
        cnt += 1
        n //= p
    return (n, cnt)
    
def getDivisorCount(n):
    cnt = 1
    (n, p_cnt) = getPrimeFactorCount(n, 2)
    cnt *= (p_cnt+1)
    (n, p_cnt) = getPrimeFactorCount(n, 3)
    cnt *= (p_cnt+1)
    (n, p_cnt) = getPrimeFactorCount(n, 5)
    cnt *= (p_cnt+1)
    k = 7
    i = 0
    p_cnt = 0
    while k <= n:
        if n%k == 0:
            p_cnt += 1
            n //= k
        else:
            k += inc[i]
            cnt *= (p_cnt+1)
            p_cnt = 0
            i += 1
            if i > 7: i = 0
    cnt *= (p_cnt+1)
    return cnt

div_cnt_d = {}
div_cnt_d[1] = 1
div_cnt_d[2] = 3
last_d_cnt = 2
for i in range(3, ub):
    n = i*(i+1) // 2
    d_cnt = getDivisorCount(n)
    if d_cnt > last_d_cnt:
        div_cnt_d[d_cnt] = n
        last_d_cnt = d_cnt
#print(div_cnt_d)

for _ in range(int(input())):
    c = int(input())
    if c >= 768:
        print(842161320)
    else:
        while True:
            c += 1
            if c in div_cnt_d:
                print(div_cnt_d[c])
                break

