#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy 
# Tags: Array, Two Pointers

"""
Question 26:
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # uniquified algorithms of sorted List 
        # remember to consider: in which cases do your algorithm invaild? (when len(A) <= 1)
        if len(A) <= 1:
            return len(A)
            # two tricks:
            # 1.swap numbers(O(1)) insdead of delete a slice
            # 2.to prevent list out of range, compare(finder, finder-1) rather than compare(finder, finder+1)
        pointer = finder = 1
        while finder < len(A):
            if A[finder] != A[finder - 1]:
                if finder > pointer:
                    A[pointer] = A[finder]
                pointer += 1
            finder += 1
        return pointer