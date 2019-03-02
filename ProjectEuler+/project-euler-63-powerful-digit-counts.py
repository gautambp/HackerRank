# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-63-powerful-digit-counts/problem

n = int(input())
ul = 10 ** n
ll = 10 ** (n-1)
r_min = int(ll ** (1.0/n))-1
r_max = int(ul ** (1.0/n))+1
for i in range(r_min, r_max):
    val = i**n
    if val > ll and val < ul:
        print(val)
