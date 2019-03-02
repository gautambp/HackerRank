# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    # your code goes here
    r = 2*size-1
    c = 4*(size-1)+1
    idx = ord('a')
    arr = []
    s = ''
    is_first = True
    for i in range(idx+size-1, idx-1, -1):
        if is_first:
            s += chr(i)
            arr.append(s.center(c, '-'))
            s += '-'
            is_first = False
        else:
            arr.append((s + chr(i) + s[::-1]).center(c, '-'))
            s += chr(i) + '-'
    for s in arr:
        print(s)
    for i in range(len(arr)-2, -1, -1):
        print(arr[i])

