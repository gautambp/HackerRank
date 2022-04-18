# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-230-fibonacci-words/problem
for _ in range(int(input())):
    s = input().split()
    a, b, n = s[0], s[1], int(s[2])
    pos_val = -1
    al = len(a)
    bl = len(b)
    ll = []
    ll.append(al)
    ll.append(bl)
    while True:
        abl = al+bl
        ll.append(abl)
        al, bl = bl, abl
        if n < bl: break
    idx = len(ll)-3
    cur_idx = idx
    while idx >= 0:
        idx_val = ll[idx]
        if n > idx_val:
            n -= idx_val
            idx -= 1
            cur_idx = idx
        else:
            if idx == 0: pos_val = a[n-1]
            elif idx == 1: pos_val = b[n-1]
            idx = cur_idx - 2
            cur_idx = idx
    if pos_val == -1:
        pos_val = b[n-1]
    print(pos_val)

        
