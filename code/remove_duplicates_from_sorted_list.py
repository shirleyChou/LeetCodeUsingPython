#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy
# Tags: Linked List

"""
Question 83:
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        else:
            go = head
            while go.next:
                if go.val != go.next.val:
                    go = go.next
                else:
                    go.next = go.next.next
            return head
