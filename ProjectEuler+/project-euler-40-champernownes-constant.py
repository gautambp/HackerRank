# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-40-champernownes-constant/problem
ub = 20
dl_cache = [10 ** dl for dl in range(ub)]
dlse_cache = [None]*ub

def find_dl_s_e(n):
    l = 1
    r = len(dlse_cache)-1
    while l < r:
        m = (l+r)//2
        #print('{} {} {}'.format(l, m, r))
        if dlse_cache[m][1] > n:
            r = m
        else:
            l = m+1
    #print(dlse_cache[r-1])
    return dlse_cache[r-1]

def init():
    s = 0
    e = 0
    for dl in range(1, ub):
        dls = dl*(dl_cache[dl] - dl_cache[dl-1])
        s, e = e+1, e+dls
        dlse_cache[dl] = (dl, s, e)

def calc_num(dl, idx):
    sn = dl_cache[dl-1]
    n = sn + ((idx-1)//dl)
    i = idx - (n - sn)*dl
    return (n, i)

init()
for _ in range(int(input())):
    s = input()
    il = list(map(int, s.split()))
    p = 1
    for i in il:
        dl, s, e = find_dl_s_e(i)
        n, idx = calc_num(dl, i-s+1)
        p *= int(str(n)[idx-1])
    print(p)

