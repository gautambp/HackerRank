# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/is-this-a-binary-search-tree/problem
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def inOrderTraverse(n):
        l1 = (inOrderTraverse(n.left) if n.left else [])
        l1.append(n.data)
        l2 = (inOrderTraverse(n.right) if n.right else [])
        return l1 + l2
    l = inOrderTraverse(root)
    for i in range(1, len(l)):
        if l[i] <= l[i-1]:
            return False
    return True
        