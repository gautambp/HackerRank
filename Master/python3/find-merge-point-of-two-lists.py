# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/find-merge-point-of-two-lists/problem


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    l = []
    while head1:
        l.append(head1)
        head1 = head1.next
    while head2:
        if head2 in l:
            return head2.data
        head2 = head2.next
    return ''

