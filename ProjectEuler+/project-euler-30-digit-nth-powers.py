# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-30-digit-nth-powers/problem
from itertools import permutations, combinations

digit_pwr_d = {
        3: [0, 1,  8,  27,   64,   125,   216,    343,    512,    729], 
        4: [0, 1, 16,  81,  256,   625,  1296,   2401,   4096,   6561], 
        5: [0, 1, 32, 243, 1024,  3125,  7776,  16807,  32768,  59049], 
        6: [0, 1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441]
}

lu_bound_d = { 3:(100, 500), 4:(1000, 10000), 5:(4000, 200000), 6:(500000,600000) }

def digitPowerSum(n, p):
    psum = 0
    for i in str(n):
        psum += digit_pwr_d[p][int(i)]
    return psum
    
n = int(input())
lb = lu_bound_d[n][0]
ub = lu_bound_d[n][1]
all_digit_pow_sum = 0
for i in range(lb, ub):
    if digitPowerSum(i, n) == i:
        all_digit_pow_sum += i
print(all_digit_pow_sum)
