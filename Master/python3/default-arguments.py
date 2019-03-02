# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/default-arguments/problem


def print_from_stream(n, stream=None):
    if stream == None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

