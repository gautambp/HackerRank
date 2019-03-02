# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/xml2---find-the-maximum-depth/problem


maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level > maxdepth:
        maxdepth = level
    for c in elem:
        depth(c, level)

