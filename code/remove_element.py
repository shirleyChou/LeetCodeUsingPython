#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/remove-element/
# Difficulty: Easy 
# Tags: Array, Two Pointers

"""
Question 27:
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        A.sort()
        for i,j in [(k,list(g)) for k, g in itertools.groupby(A)]:
            if i == elem:
                del A[A.index(i):A.index(i)+len(j)]
        