# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/print-in-reverse/problem


# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if head:
        reversePrint(head.next)
        print(head.data)

