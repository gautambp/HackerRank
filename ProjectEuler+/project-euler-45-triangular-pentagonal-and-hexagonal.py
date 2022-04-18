# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-45-triangular-pentagonal-and-hexagonal/problem
ph = [1, 165, 31977, 6203341, 1203416145, 233456528757]
tp = [1, 20, 285, 3976, 55385, 771420, 10744501, 149651600, 
      2084377905, 29031639076, 404358569165, 5631988329240]

N, a, b = list(map(int, input().split()))
if a == 3 and b == 5:
    idx = 0
    while True:
        val = tp[idx]*(tp[idx]+1)//2
        if val >= N:
            break
        print(val)
        idx += 1
else:
    idx = 0
    while True:
        val = ph[idx]*(3*ph[idx]-1)//2
        if val >= N:
            break
        print(val)
        idx += 1
