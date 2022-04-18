# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-61-cyclical-figurate-numbers/problem
from collections import defaultdict
from itertools import permutations

def get_input():
    n = int(input())
    t = list(map(int, input().split()))
    return (n, t)

def get_test():
    return (3, [3, 4, 5])
    
def init_p3_list():
    l = [False]*10001
    for i in range(40,150):
        p3 = i * (i+1) // 2
        if p3 >= 1000 and p3 < 10000:
            l[p3] = True
    return l

def init_p4_list():
    l = [False]*10001
    for i in range(30,101):
        p4 = i ** 2
        if p4 >= 1000 and p4 < 10000:
            l[p4] = True
    return l
    
def init_p5_list():
    l = [False]*10001
    for i in range(25,85):
        p5 = i * (3*i-1) // 2
        if p5 >= 1000 and p5 < 10000:
            l[p5] = True
    return l

def init_p6_list():
    l = [False]*10001
    for i in range(20,72):
        p6 = i * (2*i-1)
        if p6 >= 1000 and p6 < 10000:
            l[p6] = True
    return l

def init_p7_list():
    l = [False]*10001
    for i in range(20,65):
        p7 = i * (5*i-3) // 2
        if p7 >= 1000 and p7 < 10000:
            l[p7] = True
    return l

def init_p8_list():
    l = [False]*10001
    for i in range(15,60):
        p8 = i * (3*i-2)
        if p8 >= 1000 and p8 < 10000:
            l[p8] = True
    return l

matched_pairs = defaultdict(list)

def find_match(pl, idx1, idx2):
    for mn in range(1000, 10000):
        if pl[idx1][mn]:
            pre_mn = mn//100
            post_mn = mn%100
            for i in range(10, 100):
                idx = i+100*post_mn
                if pl[idx2][idx]:
                    matched_pairs[(idx1, idx2)].append((mn, idx))
                idx = i*100+pre_mn
                if pl[idx2][idx]:
                    matched_pairs[(idx2, idx1)].append((idx, mn))
    
def add_to_match(pl, k, pl_idx):
    match_l = matched_pairs[k]
    for m in match_l:
        mn = m[-1]
        post_mn = mn%100
        for i in range(10, 100):
            idx = i+100*post_mn
            if pl[pl_idx][idx]:
                matched_pairs[k + (pl_idx,)].append(m + (idx,))


fd = {3: init_p3_list, 4: init_p4_list, 5:init_p5_list, 6:init_p6_list, 7:init_p7_list, 8:init_p8_list}

n, t = get_input()
pl = [None, None, None, None, None, None, None, None, None]
for i in t: pl[i] = fd[i]()
for i in permutations(t, 2):
    find_match(pl, i[0], i[1])
for p in range(3, len(t)+1):
    for i in permutations(t, p):
        add_to_match(pl, i[:-1], i[-1])

ans = set()
for k in matched_pairs.keys():
    if len(k) == len(t):
        for comb in matched_pairs[k]:
            if comb[-1]%100 == comb[0]//100:
                if sum(comb) == sum(set(comb)):
                    ans.add(sum(comb))
for i in sorted(ans):
    print(i)
