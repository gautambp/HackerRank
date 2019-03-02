# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-23-non-abundant-sums/problem
abundant_flag = [None]*20162
abundant_no = []

def getAbundance(n):
    sum = 0
    f = int(n/2)
    while f > 0:
        if n%f == 0:
            sum += f
        f -= 1
    return sum
    
def setAbundantFlag():
    for i in range(12):
        abundant_flag[i] = 0
    abundant_flag[12] = 1
    for i in range(13, len(abundant_flag)):
        if abundant_flag[i]:
            continue
        if i%6 == 0:
            abundant_flag[i] = 1
        else:
            s = getAbundance(i)
            if s < i:
                abundant_flag[i] = 0
                continue
            if s > i:
                abundant_flag[i] = 1
            else:
                abundant_flag[i] = 0
            for j in range(2, 2000):
                k = i*j
                if k > 20161:
                    break
                abundant_flag[k] = 1

setAbundantFlag()
abundant_no = [i for i in range(1, len(abundant_flag)) if abundant_flag[i] == 1]

for _ in range(int(input())):
    n = int(input())
    if n > 20161:
        print('YES')
    else:
        found = False
        for a in abundant_no:
            if a >= n:
                break
            if abundant_flag[n-a] == 1:
                found = True
                break
        if found:
            print('YES')
        else:
            print('NO')
                
