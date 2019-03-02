# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem


# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    d = DoublyLinkedListNode(head.data)
    while head.next:        
        head = head.next
        nd = DoublyLinkedListNode(head.data)
        nd.next, d.prev = d, nd
        d = nd
    return d

