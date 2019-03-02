# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-219-skew-cost-coding/problem

class Node:
    def __init__(self, s, a, b):
        self.s = s
        self.cost = a*self.s.count('0') + b*self.s.count('1')
    def __str__(self):
        return '({} - {})'.format(self.s, self.cost)
    def __lt__(self, o):
        if self.cost == o.cost: return len(self.s) < len(o.s)
        return self.cost < o.cost
    def __gt__(self, o):
        if self.cost == o.cost: return len(self.s) > len(o.s)
        return self.cost > o.cost
    def __eq__(self, o):
        return self.cost == o.cost and len(self.s) == len(o.s)
    def __ne__(self, o):
        return not self.__eq__(o)
    def __ge__(self, o):
        return self.__gt__(o) or self.__eq__(o)
    def __le__(self, o):
        return self.__lt__(o) or self.__eq__(o)

def insertNode(l, n1):
    start_pt = 0
    end_pt = len(l)-1
    while start_pt <= end_pt:
        mid_pt = (start_pt+end_pt) // 2
        if n1 > l[mid_pt]:
            start_pt = mid_pt+1
        elif n1 < l[mid_pt]:
            end_pt = mid_pt-1
        else:
            l.insert(mid_pt, n1)
            return
    l.insert(start_pt, n1)
    
for _ in range(int(input())):
    (n,a,b) = [int(i) for i in input().strip().split(' ')]
    l = []
    while len(l) < n:
        if len(l) == 0:
            if a > b:
                l.append(Node('1', a, b))
                l.append(Node('0', a, b))
            else:
                l.append(Node('0', a, b))
                l.append(Node('1', a, b))
        else:        
            i = l.pop(0)
            insertNode(l, Node(i.s + '0', a, b))
            insertNode(l, Node(i.s + '1', a, b))
    
    print(sum([i.cost for i in l]) % 1000000007)
