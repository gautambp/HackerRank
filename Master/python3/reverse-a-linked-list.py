# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem


# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    l = SinglyLinkedList()
    while head:
        d = SinglyLinkedListNode(head.data)
        if l.head:
            d.next = l.head
        l.head = d
        head = head.next
    return l.head        

