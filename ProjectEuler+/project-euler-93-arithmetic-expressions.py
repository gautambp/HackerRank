# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-93-arithmetic-expressions/problem
# Problem - Arithmetic expressions
# https://www.hackerrank.com/contests/projecteuler/challenges/euler093/forum
from itertools import permutations, product

ops = ['+', '-', '*', '/']
op_templ_d = {
    2: ['d1 op1 d2'],
    3: ['(d1 op1 d2) op2 d3', 
        'd1 op1 (d2 op2 d3)'],
    4: ['((d1 op1 d2) op2 d3) op3 d4',
        '(d1 op1 d2) op2 (d3 op3 d4)',
        '(d1 op1 (d2 op2 d3) op3 d4)',
        'd1 op1 ((d2 op2 d3) op3 d4)',
        'd1 op1 (d2 op2 (d3 op3 d4))'],
    5: ['(((d1 op1 d2) op2 d3) op3 d4) op4 d5',
        '((d1 op1 d2) op2 d3) op3 (d4 op4 d5)',
        '((d1 op1 d2) op2 (d3 op3 d4)) op4 d5',
        '((d1 op1 (d2 op2 d3)) op3 d4) op4 d5',
        '(d1 op1 ((d2 op2 d3) op3 d4)) op4 d5',
        '(d1 op1 (d2 op2 (d3 op3 d4))) op4 d5',
        '(d1 op1 (d2 op2 d3)) op3 (d4 op4 d5)',
        '(d1 op1 d2) op2 ((d3 op3 d4) op4 d5)',
        'd1 op1 ((d2 op2 (d3 op3 d4)) op4 d5)',
        'd1 op1 (((d2 op2 d3) op3 d4) op4 d5)',
        'd1 op1 (d2 op2 ((d3 op3 d4) op4 d5))',
        'd1 op1 ((d2 op2 d3) op3 (d4 op4 d5))',
        '(d1 op1 d2) op2 (d3 op3 (d4 op4 d5))',
        'd1 op1 (d2 op2 (d3 op3 (d4 op4 d5)))']
}

def inject_values(t, dl, opl):
    for i in range(1, len(dl)+1):
        t = t.replace('d'+str(i), str(dl[i-1]))
    for i in range(1, len(opl)+1):
        t = t.replace('op'+str(i), str(opl[i-1]))
    return t

m = int(input())
digits = list(map(int, input().split(' ')))
val_flags = {}
if m > 1:
    for d in permutations(digits, m):
        for op in product(ops, repeat=m-1):
            for op_templ in op_templ_d[m]:
                t = inject_values(op_templ, d, op)
                try:
                    val = eval(t)
                    if val < 0 or val != int(val): continue
                    val_flags[int(val)] = True
                except:
                    pass
else:
    val_flags[digits[0]] = True
if 1 not in val_flags:
    print(0)
else:
    idx = 1
    while idx in val_flags:
        idx += 1
    print(idx-1)
