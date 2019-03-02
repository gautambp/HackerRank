# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/inserting-a-node-into-a-sorted-doubly-linked-list/problem


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    d = DoublyLinkedListNode(data)
    if head == None:
        return d
    h = head
    while h.data < data:
        if not h.next:
            h.next, d.prev = d, h
            return head
        h = h.next
    if not h.prev:
        d.next, h.prev = h, d
        return d
    else:
        d.prev, d.next = h.prev, h
        h.prev.next, h.prev = d, d
        return head


