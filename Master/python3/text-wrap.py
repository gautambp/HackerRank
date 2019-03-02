# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/text-wrap/problem


def wrap(string, max_width):
    result = ''
    l = int(len(string) / max_width)
    for i in range(l):
        result = result + string[i*max_width:(i+1)*max_width] + '\n'
    result = result + string[l*max_width:]
    return result

