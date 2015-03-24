#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
# Tags: Linked List

"""
Question 21:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        l3 = ListNode(0)
        tail = l3
        while l1 is not None and l2 is not None:
            # when li.val > l2.val, result = True
            result = l1.val <= l2.val
            tail.next = l1 if result else l2
            l1 = l1.next if result else l1
            l2 = l2 if result else l2.next
            tail = tail.next
            if l1 is None:
                tail.next = l2
            if l2 is None:
                tail.next = l1
        return l3.next
