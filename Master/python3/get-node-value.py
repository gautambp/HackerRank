# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/get-node-value/problem


# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getLength(head):
    l = 0
    while head:
        head = head.next
        l += 1
    return l

def getNode(head, positionFromTail):
    l = getLength(head)
    posFromHead = l-positionFromTail-1
    #print('{} {} {}'.format(l, positionFromTail, posFromHead))
    while posFromHead > 0:
        head = head.next
        posFromHead -= 1
    return head.data

