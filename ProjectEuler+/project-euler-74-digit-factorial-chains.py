# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-74-digit-factorial-chains/problem
# Project Euler #74: Digit factorial chains
# https://www.hackerrank.com/contests/projecteuler/challenges/euler074/problem

digit_fact_l = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
max_chain_len = 61
chain_len_nums = [set() for i in range(max_chain_len)]

chain_len_cache = {0:2, 1:1, 2:1, 145:1, 169:3, 871:2, 872:2, 1454:3, 40585:1, 45361:2, 45362:2, 363601:3}
for k in chain_len_cache.keys():
    v = chain_len_cache[k]
    chain_len_nums[v].add(k)

def digit_fact_sum(n):
    s = 0
    while n > 0:
        s += digit_fact_l[n%10]
        n = n//10
    return s

def find_chain(n, cl, idx, max_cl_len):
    if len(cl) >= max_cl_len: return -1
    if n in chain_len_cache:
        return chain_len_cache[n]+idx
    cl.append(n)
    new_n = digit_fact_sum(n)
    if new_n in cl:
        return len(cl)
    result = find_chain(new_n, cl, idx+1, max_cl_len)
    if result > 0 and n not in chain_len_cache:
        n_chain_len = result-idx
        chain_len_cache[n] = n_chain_len
        chain_len_nums[n_chain_len].add(n)
    return result

def find_chain_len(n, max_len):
    cl = []
    return find_chain(n, cl, 0, max_len)
    #print(cl)
    #if found: return len(cl)
    #return -1

def process(n, max_len):
    for i in range(3, n+1):
        if i not in chain_len_cache:
            i_chain_len = find_chain_len(i, max_len)
            chain_len_cache[i] = i_chain_len
            chain_len_nums[i_chain_len].add(i)

for _ in range(int(input())):
    s = input().split()
    n, l = int(s[0]), int(s[1])
    process(n, max_chain_len)
    found = False
    for chn in sorted(chain_len_nums[l]):
        if chn <= n:
            found = True
            print(chn, end=' ')            
    if found:
        print()
    else:
        print(-1)

