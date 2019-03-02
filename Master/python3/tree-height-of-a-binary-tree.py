# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    def recHeight(n):
        lh = (recHeight(n.left) if n.left else 0)
        rh = (recHeight(n.right) if n.right else 0)
        return (lh+1 if lh > rh else rh+1)
    return recHeight(root)-1

