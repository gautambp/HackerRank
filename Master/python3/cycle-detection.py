# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/cycle-detection/problem


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    l = []
    while head:
        if head in l:
            return 1
        l.append(head)
        head = head.next
    return 0

