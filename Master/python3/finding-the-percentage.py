# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem
from functools import reduce;

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_score = student_marks[query_name]
    score_avg = reduce(lambda x, y: x+y, student_score) / len(student_score);
    print('{:.2f}'.format(score_avg))


