# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    while True:
        if not head:
            break;
        print(head.data)
        head = head.next

