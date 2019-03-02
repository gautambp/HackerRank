# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/delete-a-node/problem


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if position == 0:
        return head.next
    h = head
    while position > 1:
        h = h.next
        position -= 1
    h.next = h.next.next
    return head

