# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-225-tribonacci-non-divisors/problem
ub = 100000

def get_input():
    return list(map(int, input().split()))
    #return (1, 1, 1, 10)

def trib_gen(t1, t2, t3, n):
    while True:
        tn = t1+t2+t3
        t3, t2, t1 = tn%n, t3, t2
        yield (t3, t2, t1)

t1, t2, t3, k = get_input()
tss = (t3, t2, t1)
ans = None
n = 1
while k > 0:
    n += 2
    tg = trib_gen(t1, t2, t3, n)
    found = True
    for i in range(ub):
        ts = next(tg)
        if ts[0] == 0:
            found = False
            break
        elif ts == tss:
            break
    if found:
        #print('{} {}'.format(k, n))
        ans = n
        k -= 1
print(ans)
