# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-46-goldbachs-other-conjecture/problem
ub = 500000
prime_flag_l = [False]*ub
prime_flag_l[2] = prime_flag_l[3] = prime_flag_l[5] = prime_flag_l[7] = True
prime_last_no = 7
double_sqr_l = []
last_double_sqr_idx = 1

def is_prime(n):
    if n % 2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0:
         return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

def init_prime_flags(n):
    global prime_last_no
    global prime_flag_l
    while n > prime_last_no:
        prime_last_no += 2
        prime_flag_l[prime_last_no] = is_prime(prime_last_no)

def init_double_sqr(n):
    global last_double_sqr_idx
    global double_sqr_l
    while True:
        val = 2*last_double_sqr_idx*last_double_sqr_idx
        double_sqr_l.append(val)
        last_double_sqr_idx += 1
        if val > n:
            break

for _ in range(int(input())):
    n = int(input())
    init_prime_flags(n)
    init_double_sqr(n)
    cnt = 0
    i = 0
    while i < len(double_sqr_l):
        d = n-double_sqr_l[i]
        if d < 3:
            break
        if prime_flag_l[d]:
            cnt += 1
        i += 1
    print(cnt)
