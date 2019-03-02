# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    d = {}
    #Write your code here
    def recLevelOrder(n):
        if n.left:
            if not n.left.level:
                n.left.level = n.level+1
            recLevelOrder(n.left)
        if n.right:
            if not n.right.level:
                n.right.level = n.level+1
            recLevelOrder(n.right)
        if n.level in d:
            d[n.level].append(n.info)
        else:
            d[n.level] = [n.info]
    root.level = 0
    recLevelOrder(root)
    l = 0
    while len(d) > 0:
        for i in d[l]:
            print(i, end=' ')
        del d[l]
        l += 1


