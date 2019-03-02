# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    s_len = len(string)
    p = int(s_len/k)
    s = ''
    l = 0
    for i in range(s_len):
        if l < k:
            if s.find(string[i]) < 0:
                s += string[i]
            l += 1
            if l == k:
                print(s)
                l = 0
                s = ''
        

