# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-206-concealed-square/problem
import math

def get_input():
    n = int(input())
    dl = input().split()
    return (n, dl)

def get_test():
    #return (3, ['8','7','6'])
    #return (4, ['1','2','3','4'])
    #return (7, ['1','2','1','5','7','4','9'])
    return (9, ['1','2','1','7','7','0','9','5','1'])

def get_bounds(dl):
    high_no = ''
    low_no = ''
    is_first = True
    for i in dl:
        if is_first: is_first = False
        else:
            high_no += '9'
            low_no += '0'
        high_no += i
        low_no += i
    return math.sqrt(int(high_no)), math.sqrt(int(low_no))

def is_match(n, dl, ns):
    for i in range(n):
        if dl[i] != ns[2*i]: return False
    return True

def find_match(n, dl, lb, hb):
    for i in range(lb, hb, 10):
        if is_match(n, dl, str(i**2)):
            return i
    return None

def reduce_to_match_last_digit(n, d):
    while n%10 != d:
        n += 1
    return n

n, dl = get_input()
hb, lb = get_bounds(dl)
hb, lb = math.floor(hb), math.ceil(lb)
found_match = None
last_digit = int(dl[-1])
if last_digit == 0:
    lb = reduce_to_match_last_digit(lb, 0)
    found_match = find_match(n, dl, lb, hb)
elif last_digit == 1:
    lb = reduce_to_match_last_digit(lb, 9)
    found_match = find_match(n, dl, lb, hb)
    if found_match == None:
        lb = lb - 8
        found_match = find_match(n, dl, lb, hb)
elif last_digit == 4:
    lb = reduce_to_match_last_digit(lb, 8)
    found_match = find_match(n, dl, lb, hb)
    if found_match == None:
        lb = lb - 6
        found_match = find_match(n, dl, lb, hb)
elif last_digit == 5:
    lb = reduce_to_match_last_digit(lb, 5)
    found_match = find_match(n, dl, lb, hb)
elif last_digit == 6:
    lb = reduce_to_match_last_digit(lb, 6)
    found_match = find_match(n, dl, lb, hb)
    if found_match == None:
        lb = lb - 2
        found_match = find_match(n, dl, lb, hb)
elif last_digit == 9:
    lb = reduce_to_match_last_digit(lb, 7)
    found_match = find_match(n, dl, lb, hb)
    if found_match == None:
        lb = lb - 4
        found_match = find_match(n, dl, lb, hb)

print(found_match)
