# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem


# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    d = SinglyLinkedListNode(data)
    h = head
    while position > 1:
        h = h.next
        position -= 1
    d.next = h.next
    h.next = d
    return head


