# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/string-formatting/problem
def print_formatted(number):
    l = len(bin(number))-2
    for i in range(1, number+1):
        d_val = str(i)
        o_val = oct(i)[2:]
        h_val = hex(i)[2:]
        h_val = h_val.upper()
        b_val = bin(i)[2:]
        print("{} {} {} {}".format(d_val.rjust(l), o_val.rjust(l), h_val.rjust(l), b_val.rjust(l)))

