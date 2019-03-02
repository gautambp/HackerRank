# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/find-the-runner-up-score--/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner = -101;
    runnerup = -101;
    for s in arr:
        if s > winner:
            runnerup = winner;
            winner = s;
        elif s > runnerup and not(s == winner):
            runnerup = s;
    print(runnerup);
    