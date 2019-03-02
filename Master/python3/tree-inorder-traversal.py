# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree-inorder-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root.left: inOrder(root.left)
    print(root.info, end=' ')
    if root.right: inOrder(root.right)
    #Write your code here

