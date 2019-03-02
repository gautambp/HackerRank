# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/ProjectEuler+/project-euler-22-names-scores/problem
a_ord = ord('A')-1
names = []
for _ in range(int(input())):
    names.append(input())
sorted_names = sorted(names)
for _ in range(int(input())):
    name = input()
    name_idx = None
    for idx in range(len(sorted_names)):
        if name == sorted_names[idx]:
            name_idx = idx+1
            break
    name_sum = sum(map(lambda x: ord(x)-a_ord, name))
    print(name_sum * name_idx)
