# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree--top-view/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    print(root.info, end=' ')
    if root.right: topView(root.right)

