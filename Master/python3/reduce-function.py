# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/reduce-function/problem


def product(fracs):
    t = Fraction(reduce(lambda p,f: p*f.numerator, fracs, 1), reduce(lambda p,f: p*f.denominator, fracs, 1))
    return t.numerator, t.denominator

