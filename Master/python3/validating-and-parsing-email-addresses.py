# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-and-parsing-email-addresses/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils


def isExtValid(ext):
    if len(ext) > 3: return False
    if any([not c.isalpha() for c in ext]): return False
    return True

def isDomainValid(d):
    if any([not c.isalpha() for c in d]): return False
    return True

def isUsernameValid(u):
    if not u[0].isalpha(): return False
    if any([not (c.isalnum() or c == '-' or c == '_' or c == '.') for c in u]): return False
    return True

def isEmailValid(e):
    s = e.split('@')
    if len(s) != 2: return False
    u = s[0]
    ss = s[1].split('.')
    if len(ss) != 2: return False
    d = ss[0]
    ext = ss[1]
    return isUsernameValid(u) and isDomainValid(d) and isExtValid(ext)

for _ in range(int(input())):
    os = input()
    s = os.split()
    ss = s[1].split('<')
    e = ss[1][:-1]
    if isEmailValid(e):
        #print(email.utils.parseaddr(s))
        print(os)

