# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-4-largest-palindrome-product/problem
l = []
for i in range(9, 0, -1):
    for j in range(9, -1, -1):
        for k in range(9, -1, -1):
            no = 100000*i + 10000*j + 1000*k + 100*k + 10*j + i
            for m in range(100, int(no**0.5)+1):
                if no%m == 0:
                    d = int(no/m)
                    if d > 99 and d < 1000:
                        l.append(no)
                        break

for _ in range(int(input())):
    n = int(input())
    for i in l:
        if i >= n: continue
        print(i)
        break
