# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/any-or-all/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPalindrome(n):
    s = str(n)
    s_len = len(s)
    if s_len == 1:
        return True
    else:
        for i in range(s_len):
            if s[i] != s[s_len-i-1]:
                return False
    return True

n = int(input())
l = [int(i) for i in input().split(' ')]
print(all([i > 0 for i in l]) and any([isPalindrome(i) for i in l]))
