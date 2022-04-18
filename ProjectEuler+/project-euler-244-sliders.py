# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-244-sliders/problem
import sys
   
def get_inputs():
    n = int(input())
    s = ''
    e = ''
    for i in range(n):
        s += input()
    for i in range(n):
        e += input()
    return (n, s, e)

def get_test():
    #return (2, 'WRBB', 'RBBW')
    return (3, 'BBBBWRRRR', 'RBRBWBRBR')
    #return (4, 'WRBBRRBBRRBBRRBB', 'RRBBRBBBRWRBRRBB')

def moveR(n, g):
    idx = g.find('W')
    if idx%n == 0: return None
    return g[:idx-1] + g[idx] + g[idx-1] + g[idx+1:]

def moveL(n, g):
    idx = g.find('W')
    if idx%n == n-1: return None
    return g[:idx] + g[idx+1] + g[idx] + g[idx+2:]

def moveD(n, g):
    idx = g.find('W')
    if idx//n == 0: return None
    return g[:idx-n] + g[idx] + g[idx-n+1:idx] + g[idx-n] + g[idx+1:]

def moveU(n, g):
    idx = g.find('W')
    if idx//n == n-1: return None
    return g[:idx] + g[idx+n] + g[idx+1:idx+n] + g[idx] + g[idx+n+1:]

all_move_funcs = {'R':moveR, 'L':moveL, 'D':moveD, 'U':moveU}
all_sol_l = []
n, s, e = get_inputs()
to_visit = [(s, '')]
visited = {}
while len(to_visit) > 0:
    new_to_visit = []
    for g, steps in to_visit:
        if g == e:
            all_sol_l.append(steps)
        else:
            if g in visited:
                if visited[g] < len(steps):
                    continue
            else:
                visited[g] = len(steps)
            for mk in all_move_funcs.keys():
                mf = all_move_funcs[mk]
                new_g = mf(n, g)
                if new_g == None: continue
                new_to_visit.append((new_g, steps + mk))
    to_visit = new_to_visit

min_sol_len = sys.maxsize
for sol in all_sol_l:
    if len(sol) < min_sol_len: min_sol_len = len(sol)

checksum = 0
for sol in all_sol_l:
    if len(sol) > min_sol_len: continue
    cs = 0
    for ch in sol:
        cs = (cs * 243 + ord(ch)) % 100000007
    checksum = (checksum + cs) % 100000007
print(checksum)
