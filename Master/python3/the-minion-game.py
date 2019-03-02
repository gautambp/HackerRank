# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/the-minion-game/problem
def isVowel(c):
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        return True
    return False

def minion_game(string):
    # your code goes here
    k_score = 0
    s_score = 0
    s_len = len(string)
    for i in range(s_len):
        if isVowel(string[i]):
            k_score += (s_len-i)
        else:
            s_score += (s_len-i)
    if k_score > s_score:
        print('Kevin', k_score)
    elif s_score > k_score:
        print('Stuart', s_score)
    else:
        print('Draw')

