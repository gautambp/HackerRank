# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-57-square-root-convergents/problem

def getNewFractions(n, d, m):
    return (d, m*d+n)

def getFractions():
    n = 1
    d = 2
    while True:
        yield getNewFractions(n, d, 1)
        (n, d) = getNewFractions(n, d, 2)

n = int(input())
g = getFractions()
for i in range(1, n+1):
    (den, num) = next(g)
    if len(str(den)) != len(str(num)):
        print(i)

