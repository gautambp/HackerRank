# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/decorators-2---name-directory/problem


def person_lister(f):
    def inner(people):
        # complete the function
        return list(map(lambda p: f(p), sorted(people,key=lambda x: int(x[2]))))
    return inner

