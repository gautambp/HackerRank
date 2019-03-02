# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-15-lattice-paths/problem
routeCount = [None]*501
for i in range(501):
    routeCount[i] = [None]*501

def cache(n, m, s):
    routeCount[n][m] = s
    routeCount[m][n] = s
    
def countRoute(n, m):
    if routeCount[n][m]:
        return routeCount[n][m]
    if n == 0:
        return 1
    if m == 0:
        return 1
    n1 = 0
    if routeCount[n-1][m]:
        n1 = routeCount[n-1][m]
    else:
        n1 = countRoute(n-1, m)
        cache(n-1, m, n1)
    n2 = 0
    if routeCount[n][m-1]:
        n2 = routeCount[n][m-1]
    else:
        n2 = countRoute(n, m-1)
        cache(n, m-1, n2)
    cache(n, m, n1+n2)
    return n1 + n2

for _ in range(int(input().strip())):
    (ns, ms) = input().split(' ')
    n = int(ns)
    m = int(ms)
    print(countRoute(n, m) % 1000000007)

