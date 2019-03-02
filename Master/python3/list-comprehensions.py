# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print("[", end='');
    first = False
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != n:
                    if first == False:
                        print('[{}, {}, {}]'.format(i, j, k), end='');
                        first = True;
                    else:
                        print(', [{}, {}, {}]'.format(i, j, k), end='');
    print(']');    