# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-56-powerful-digit-sum/problem
n = int(input())
l = [str(a ** b) for a in range(2, n) for b in range(2, n)]
s = max(map(lambda x: sum(int(d) for d in x), l))
print(s)
