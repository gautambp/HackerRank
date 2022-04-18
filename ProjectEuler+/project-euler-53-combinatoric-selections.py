# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-53-combinatoric-selections/problem
def get_count(n, k):
    cnt = 0
    l = [1]
    idx = 0
    while idx < n:
        new_l = [1]
        for i in range(len(l)):
            if i > 0:
                val = l[i-1]+l[i]
                new_l.append(val)
                if val > k: cnt += 1
            if i == len(l)-1:
                new_l.append(1)
        l = new_l
        idx += 1    
    return cnt

s = input().split()
print(get_count(int(s[0]),int(s[1])))
