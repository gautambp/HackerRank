# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    print(root.info, end=' ')
    if root.left: preOrder(root.left)
    if root.right: preOrder(root.right)

