# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    if llist1 == None and llist2 == None: return 1
    if llist1 == None or llist2 == None: return 0
    if llist1.data != llist2.data: return 0
    return compare_lists(llist1.next, llist2.next)

