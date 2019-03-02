# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/set-discard-remove-&-pop/problem
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    ops = input().split()
    if ops[0] == 'pop':
        if len(s) > 0:
            s.pop()
    elif ops[0] == 'remove':
        i = int(ops[1])
        if i in s:
            s.remove(i)
    elif ops[0] == 'discard':
        s.discard(int(ops[1]))

print(sum(s))
