# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem


# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    last_val = head.data
    h = head
    while h.next:
        if h.next.data == last_val:
            h.next = h.next.next
        else:
            last_val = h.next.data
            h = h.next
    return head

