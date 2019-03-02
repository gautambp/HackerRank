# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-54-poker-hands/problem

class card:
    def __init__(self, s):
        self.suite = s[1]
        if s[0] == 'T': 
            self.rank = 10
        elif s[0] == 'J':
            self.rank = 11
        elif s[0] == 'Q':
            self.rank = 12
        elif s[0] == 'K':
            self.rank = 13
        elif s[0] == 'A':
            self.rank = 14
        else:
            self.rank = int(s[0])
    def isNext(self, o):
        diff = abs(self.rank - o.rank)
        if diff == 1:
            return True
        return False
    def isAce(self):
        return self.rank == 14
    def isKing(self):
        return self.rank == 13
    def __str__(self):
        return str(self.rank) + self.suite
    def __eq__(self, o):
        return self.rank == o.rank
    def __ne__(self, o):
        return not self.__eq__(o)    
    def __lt__(self, o):
        return self.rank < o.rank
    def __le__(self, o):
        return self.__lt__(o) or self.__eq__(o)
    def __gt__(self, o):
        return self.rank > o.rank
    def __ge__(self, o):
        return self.__ge__(o) or self.__eq__(o)
        
class hand:
    def __init__(self, p):
        self.c = list()
        for i in range(5):
            self.c.append(card(p[i]))
        self.c.sort()
    def __str__(self):
        s = ''
        for c in self.c: s += c.__str__() + ' '
        return s 
    def isOnePair(self):
        for i in range(4):
            if self.c[i] == self.c[i+1]:
                return (True, self.c[i])
        return (False, None)
    def isTwoPair(self):
        next_i = -1
        for i in range(4):
            if self.c[i] == self.c[i+1]:
                next_i = i+2
                break
        if next_i < 0:
            return (False, None, None)
        for i in range(next_i, 4):
            if self.c[i] == self.c[i+1]:
                return (True, self.c[i], self.c[next_i-2])
        return (False, None, None)
    def isThreeOfAKind(self):
        for i in range(3):
            if self.c[i] == self.c[i+1] and self.c[i] == self.c[i+2]:
                return (True, self.c[i])
        return (False, None)
    def isFourOfAKind(self):
        for i in range(2):
            if self.c[i] == self.c[i+1] and self.c[i] == self.c[i+2] and self.c[i] == self.c[i+3]:
                return (True, self.c[i])
        return (False, None)
    def isStraight(self):
        for i in range(3):
            if not self.c[i].isNext(self.c[i+1]):
                return (False, None)
        if self.c[4].isAce():
            if self.c[3].isKing():
                return (True, self.c[4])
            if self.c[3].rank == 5:
                return (True, self.c[3])
            else:
                return (False, None)
        else:
            return (self.c[3].isNext(self.c[4]), self.c[4])
    def isFlush(self):
        for i in range(4):
            if self.c[i].suite != self.c[i+1].suite:
                return (False, None)
        return (True, None)
    def isFullHouse(self):
        t = None
        for i in range(3):
            if self.c[i] == self.c[i+1] and self.c[i] == self.c[i+2]:
                t = self.c[i]
        if not t:
            return (False, None, None)
        for i in range(4):
            if self.c[i] != t and self.c[i] == self.c[i+1]:
                return (True, t, self.c[i])
        return (False, None, None)
    def isRoyalFlush(self):
        if not self.isFlush()[0]:
            return (False, None)
        for i in range(5):
            if self.c[i].rank != 10+i:
                return (False, None)
        return (True, None)
    def isStraightFlush(self):
        return (self.isStraight()[0] and self.isFlush()[0], self.c[4])

def compareHighCard(p1h, p2h):
    for i in range(4, -1, -1):
        if p1h.c[i].rank > p2h.c[i].rank:
            return p1h
        elif p2h.c[i].rank > p1h.c[i].rank:
            return p2h
    return None

def compareHigherWin(p1h, p1w, p2h, p2w):
    for i in range(1, 3):
        if (len(p1w) < i+1 and len(p2w) < i+1) or not(p1w[i] or p2w[i]):
            continue
        if len(p1w) < i+1 or not p1w[i]:
            return p2h
        if len(p2w) < i+1 or not p2w[i]:
            return p1h
        if p1w[i] > p2w[i]:
            return p1h
        elif p1w[i] < p2w[i]:
            return p2h
    return compareHighCard(p1h, p2h)
    
win_conditions = [
        hand.isRoyalFlush,
        hand.isStraightFlush,
        hand.isFourOfAKind,
        hand.isFullHouse,
        hand.isFlush,
        hand.isStraight,
        hand.isThreeOfAKind,
        hand.isTwoPair,
        hand.isOnePair
]
def findWinner(p1h, p2h):
    for w in win_conditions:
        p1w = w(p1h)
        p2w = w(p2h)
        if not(p1w[0] or p2w[0]): 
            continue
        if p1w[0] and not p2w[0]: 
            return p1h
        elif p2w[0] and not p1w[0]:
            return p2h
        else:
            wh = compareHigherWin(p1h, p1w, p2h, p2w)
            if wh == p1h:
                return p1h
            else:
                return p2h
    return compareHighCard(p1h, p2h)
        
for _ in range(int(input())):
    s = '4D 6S 9H QH QC 3D 6D 7H QD QS'.split(' ')
    s = input().strip().split(' ')
    p1 = [s[0], s[1], s[2], s[3], s[4]]
    p2 = [s[5], s[6], s[7], s[8], s[9]]
    p1h = hand(p1)
    p2h = hand(p2)
    w = findWinner(p1h, p2h)
    if w == p1h:
        print('Player 1')
    else:
        print('Player 2')
