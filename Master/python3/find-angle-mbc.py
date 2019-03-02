# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/find-angle-mbc/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())

print(str(int(round(math.degrees(math.atan2(ab,bc)))))+'°')