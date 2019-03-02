# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-222-sphere-packing/problem

(pr, n) = [int(i) for i in input().split(' ')]
l = [int(i) for i in input().split(' ')]

def calcDistance(r1, r2, pr):
    rt = r1 + r2
    pd = 2*pr
    return ((2*pd*rt - pd*pd) ** 0.5)
    
if n > 1:
    sl = []
    is_append = False
    for i in sorted(l):
        if len(sl) == 0:
            sl.append(i)
        elif is_append:
            sl.append(i)
            is_append = False
        else:
            sl.insert(0, i)
            is_append = True
    c_sum = sl[0]
    for i in range(1,n):
        c_sum += calcDistance(sl[i-1], sl[i], pr)
    c_sum += sl[n-1]
    print(round(c_sum*1000))
else:
    print(round(2*l[0]*1000))

