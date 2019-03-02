# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-31-coin-sums/problem
coinSumCache = [0]*100001

def coinSum(m, coins):
    if m < 0:
        return 0
    elif len(coins) == 0:
        return 0
    elif m == 0:
        return 1
    else:
        s1 = coinSum(m, coins[1:])
        s2 = coinSum(m - coins[0], coins)
        return s1 + s2

def init():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coinSumCache[0] = 1
    for c in coins:
        for m in range(c, 100001):
            coinSumCache[m] += coinSumCache[m-c]

init()
for _ in range(int(input())):
    m = int(input())
    print(coinSumCache[m] % 1000000007)
    