# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree-huffman-decoding-/problem


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    idx = 0
	#Enter Your Code Here
    def recDecodeHuff(n):
        nonlocal idx
        if n.left == None and n.right == None:
            return n.data
        if s[idx] == '0':
            idx += 1
            return recDecodeHuff(n.left)
        else:
            idx += 1
            return recDecodeHuff(n.right)
    ds = ''
    while idx < len(s):
        ds += recDecodeHuff(root)
    print(ds)

