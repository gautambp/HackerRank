# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/binary-search-tree--lowest-common-ancestor/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
    def findParents(n, v):
        if n.info == v: return [n]
        if n.left == None and n.right == None: return []
        ll = (findParents(n.left, v) if n.left else None)
        if ll: return ll + [n]
        lr = (findParents(n.right, v) if n.right else None)
        if lr: return lr + [n]
        return []
    v1_pl = findParents(root, v1)
    v2_pl = findParents(root, v2)
    for n in v1_pl:
        if n in v2_pl:
            return n

