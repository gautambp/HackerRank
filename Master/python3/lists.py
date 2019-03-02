# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/lists/problem
if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        aLine = input();
        parts = aLine.split();
        cmd = parts[0]
        if cmd == 'insert':
            idx = int(parts[1])
            val = int(parts[2])
            l.insert(idx, val)
        elif cmd == 'append':
            val = int(parts[1])
            l.append(val)
        elif cmd == 'print':
            print(l);
        elif cmd == 'remove':
            val = int(parts[1])
            l.remove(val)
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'sort':
            l.sort()
        elif cmd == 'reverse':
            l.reverse()

