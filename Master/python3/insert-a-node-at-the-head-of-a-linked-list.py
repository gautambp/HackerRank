# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    # Write your code here
    d = SinglyLinkedListNode(data)
    if not head:
        return d
    d.next = head
    return d 
    

