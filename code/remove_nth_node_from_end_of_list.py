#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Easy
# Tags: Linked List, Two Pointers

"""
Question 19:
Given a linked list,
remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        node = head
        go = head
        count = 0
        while node:
            count += 1
            node = node.next
            if count-1 > n:
                go = go.next
        if count == n:
            head = head.next
        else:
            go.next = go.next.next
        return head
