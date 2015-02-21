#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/largest-number/
# Difficulty: Medium 
# Tags: Sort

"""
Question 179:
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # map(func,sequence) excute func on all elements of sequence
        num = map(str, num)
        num.sort(cmp=lambda x,y: cmp(x+y,y+x), reverse=True)
        # int(): to aviod [0,0] --> "00"
        return str(int(''.join(num))) 



