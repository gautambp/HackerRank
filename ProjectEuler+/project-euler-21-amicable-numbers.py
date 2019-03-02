# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-21-amicable-numbers/problem
amicable_pairs = [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856), (12285, 14595), (17296, 18416), (63020, 76084), (66928, 66992), (67095, 71145), (69615, 87633), (79750, 88730)]

for _ in range(int(input())):
    n = int(input())
    sum = 0
    for j in amicable_pairs:
        if j[0] < n:
            sum += j[0]
        if j[1] < n:
            sum += j[1]
    print(sum)
