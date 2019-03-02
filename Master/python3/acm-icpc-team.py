# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/acm-icpc-team/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def strOrSubCount(s1, s2):
    sub_cnt = 0
    for i in range(len(s1)):
        if s1[i] == '1' or s2[i] == '1':
            sub_cnt += 1
    return sub_cnt

def acmTeam(topic):
    max_topic = 0
    max_topic_cnt = 0
    for i in range(len(topic)):
        for j in range(i+1, len(topic)):
            t = strOrSubCount(topic[i], topic[j])
            if t > max_topic:
                max_topic = t
                max_topic_cnt = 1
            elif t == max_topic:
                max_topic_cnt += 1
    return [max_topic, max_topic_cnt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
