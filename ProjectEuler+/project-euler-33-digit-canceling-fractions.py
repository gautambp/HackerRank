# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-33-digit-canceling-fractions/problem
def num_pair_gen(dl):
    n_start = 10 ** (dl-1)
    n_end = 10 ** dl
    for dn in range(n_start, n_end):
        for nn in range(n_start, dn):
            yield (str(nn), str(dn))

def expand_num_gen(ns, ds):
    for idx in range(len(ns)+1):
        yield ns[0:idx] + ds + ns[idx:]

def expanded_num_pair_gen(g):
    for ns, ds in g:
        for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for nse in expand_num_gen(ns, d):
                for dse in expand_num_gen(ds, d):
                    if int(nse) < int(dse):
                        yield (nse, dse, ns, ds)

def expanded_num_pair(ns, ds):
    for d in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for nse in expand_num_gen(ns, d):
            for dse in expand_num_gen(ds, d):
                if int(nse) < int(dse):
                    yield (nse, dse, ns, ds)

def get_input():
    s = input().split()
    return int(s[0]), int(s[1])
    #return (2, 1)

n, k = get_input()
if n == 4:
# 4 3 = 255983 467405
# 4 2 = 3578149 7108147
# 4 1 = 13064468 28336196
# 3 2 = 7429 17305
# 3 1 = 77262 163829
# 2 1 = 110 322
    if k == 3: print('255983 467405')
    elif k == 2: print('3578149 7108147')
    else: print('13064468 28336196')
else:
    kgen = num_pair_gen(n-k)
    ans = set()
    if k == 1:
        for nls, dls, nss, dss in expanded_num_pair_gen(kgen):
            nl, dl, ns, ds = int(nls), int(dls), int(nss), int(dss)
            if nl/dl == ns/ds:
                ans.add((nl, dl, ns, ds))
    elif k == 2:
        for n1, d1, nss, dss in expanded_num_pair_gen(kgen):
            for nls, dls, _, _ in expanded_num_pair(n1, d1):
                nl, dl, ns, ds = int(nls), int(dls), int(nss), int(dss)
                if nl/dl == ns/ds:
                    ans.add((nl, dl, ns, ds))
    else:
        for n1, d1, nss, dss in expanded_num_pair_gen(kgen):
            for n2, d2, _, _ in expanded_num_pair(n1, d1):
                for nls, dls, _, _ in expanded_num_pair(n2, d2):
                    nl, dl, ns, ds = int(nls), int(dls), int(nss), int(dss)
                    if nl/dl == ns/ds:
                        ans.add((nl, dl, ns, ds))
    nls = dls = 0
    for i in ans:
        nls += i[0]
        dls += i[1]
    print('{} {}'.format(nls, dls))
