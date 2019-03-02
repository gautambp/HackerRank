# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            cnt = cnt+1
    return cnt

