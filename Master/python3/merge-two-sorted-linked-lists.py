# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    mh = SinglyLinkedListNode(-1)
    m = mh
    while head1 != None or head2 != None:
        if head1 == None: 
            m.next = head2
            head2 = None
        elif head2 == None:
            m.next = head1
            head1 = None
        elif head1.data < head2.data:
            d = SinglyLinkedListNode(head1.data)
            m.next = d
            m = d
            head1 = head1.next
        else:
            d = SinglyLinkedListNode(head2.data)
            m.next = d
            m = d
            head2 = head2.next
    return mh.next

