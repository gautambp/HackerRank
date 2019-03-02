# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-59-xor-decryption/problem
from itertools import permutations
import string

allowed_chars = set(string.ascii_lowercase + string.ascii_uppercase + '0123456789' + "(;:,.'?-!) ")

n = int(input())
ch = input().strip()
ch_l = [int(i) for i in ch.split(' ')]
r = range(len(ch_l))

for pwd in permutations('abcdefghijklmnopqrstuvwxyz', 3):
    k = [ord(pwd[0]), ord(pwd[1]), ord(pwd[2])]
    found = True
    for i in r:
        dc = chr(ch_l[i] ^ k[i%3])
        if dc not in allowed_chars:
            found = False
            break
    if found:
        print(''.join(pwd))
        break
