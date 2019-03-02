# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/xml-1---find-the-score/problem


def get_attr_number(node):
    # your code goes here
    return len(node.attrib) + sum([get_attr_number(c) for c in node])

