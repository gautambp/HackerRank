# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-65-convergents-of-e/problem
n = int(input())
i = 2
a_term = 2
ai_2 = hi_2 = 2
ai_1 = 1
hi = hi_1 = (ai_2*ai_1) + 1
while i < n:
    ai = (1 if i%3 != 2 else a_term)
    hi = ai*hi_1 + hi_2
    if i%3 == 2: a_term += 2
    ai_2, ai_1 = ai_1, ai
    hi_2, hi_1 = hi_1, hi
    i += 1
if n == 1:
    print(2)
else:
    print(sum(map(int, str(hi))))
