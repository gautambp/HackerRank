# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-87-prime-power-triples/problem
ub = (10 ** 7)+1

def is_prime(n):
    if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0:
        return False
    for i in range(13, int(n**0.5), 2):
        if n%i == 0:
            return False
    return True

def get_prime_list(ub):
    p_l = [2, 3, 5, 7, 11]
    for i in range(13, int(ub ** 0.5), 2):
        if is_prime(i):
            p_l.append(i)
    return p_l

def get_num_list(ub):
    p_l = get_prime_list(ub)
    num_l = set()
    for p4i in range(len(p_l)):
        p4 = p_l[p4i]
        s4 = p4 ** 4
        if s4 > ub: break
        for p3i in range(len(p_l)):
            p3 = p_l[p3i]
            s3 = p3 ** 3
            if s3 > ub or (s3+s4) > ub: break
            for p2i in range(len(p_l)):
                p2 = p_l[p2i]
                s = s4+s3+(p2 ** 2)
                if s > ub: break
                num_l.add(s)
    return sorted(num_l)

result_l = [0]*ub
num_l = get_num_list(ub)
num_idx = 0
num_cnt = 0
for i in range(1,ub):
    if i == num_l[num_idx]:
        num_cnt += 1
        num_idx += 1
        if num_idx >= len(num_l): num_idx = len(num_l)-1
    result_l[i] = num_cnt

for _ in range(int(input())):
    n = int(input())
    print(result_l[n])

    
