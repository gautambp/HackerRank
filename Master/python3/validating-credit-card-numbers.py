# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-credit-card-numbers/problem

def isValidHyphens(s):
    p = s.split('-')
    if len(p[0]) == 4 and len(p[1]) == 4 and len(p[2]) == 4 and len(p[3]) == 4: return True
    return False
    
def isValidCC(s):
    if not(s[0] == '4' or s[0] == '5' or s[0] == '6'): return False
    if any([not(c.isdigit() or c == '-') for c in s]): return False
    if not(len(s) == 16 or len(s) == 19): return False
    if s.find('-') > 0:
        if not isValidHyphens(s): return False
        s = s.replace('-', '')
    last_ch = s[0]
    last_ch_len = 1
    for ch in s:
        if ch == last_ch:
            last_ch_len += 1
            if last_ch_len >= 4: return False
        else:
            last_ch = ch
            last_ch_len = 1
    if last_ch_len >= 4: return False
    return True
    
for _ in range(int(input())):
    os = input()
    print('Valid' if isValidCC(os) else 'Invalid')

