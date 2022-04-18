# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-64-odd-period-square-roots/problem

def get_continued_fractions(n):
    l = []
    d = {}
    a0 = int(n ** 0.5)
    a = a0
    num = 1
    den = a
    while True:
        new_num = int((n - (den ** 2))//num)
        a = int(((n ** 0.5) + den)//new_num)
        new_den = new_num*a - den
        #print('{} {} {}'.format(a1, new_num, new_den))
        num, den = new_num, new_den
        if (a, num, den) in d: break
        l.append(a)
        d[(a, num, den)] = True
    return (a0, l)

n = int(input())
odd_period_cnt = 0
for i in range(2, n+1):
    if (i ** 0.5)%1 == 0: continue
    f = get_continued_fractions(i)
    if len(f[1])%2 == 1:
        odd_period_cnt += 1
print(odd_period_cnt)
