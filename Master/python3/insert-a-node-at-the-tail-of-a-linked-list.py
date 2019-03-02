# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem


# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    n = SinglyLinkedListNode(data);
    if not head:
        return n
    h = head
    while h.next:
        h = h.next
    h.next = n
    return head

