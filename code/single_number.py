#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/single-number/
# Difficulty: Medium 
# Tags: Hash Table, Bit Manipulation

"""
Question 136:
Given an array of integers, every element appears twice except for one. Find that single one.
"""

""" sorted and compare """
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        A.sort()   # O(nlogn) 
        first = 0
        second = 1
        if len(A) == 1:
            return A[0]
        while second <= len(A):
            if A[first] != A[second]:
                return A[first]
            else:
                first += 2
                second += 2
                if first == len(A)-1:
                    return A[first]


""" One line python solution """                   
class Solution:
# @param A, a list of integer
# @return an integer
    def singleNumber(self, A):
        return reduce(lambda x, y: x ^ y, A)