# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-29-distinct-powers/problem
def test_val(n):
    s = set()
    for b in range(2,n+1):
        for p in range(2, n+1):
            s.add(b ** p)
    return len(s)

print(test_val(int(input())))
