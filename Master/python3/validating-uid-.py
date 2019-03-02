# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-uid-/problem

def isValidUID(s):
    if len(s) != 10: return False
    u_cnt = 0
    d_cnt = 0
    d = {}
    for c in s:
        if c.isupper(): u_cnt += 1
        if c.isdigit(): d_cnt += 1
        if not c.isalnum(): return False
        if c not in d: d[c] = 1
        else: return False
    if u_cnt < 2: return False
    if d_cnt < 3: return False
    return True
    
for _ in range(int(input())):
    os = input()
    print('Valid' if isValidUID(os) else 'Invalid')

