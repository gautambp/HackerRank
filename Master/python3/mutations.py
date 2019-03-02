# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/mutations/problem
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

