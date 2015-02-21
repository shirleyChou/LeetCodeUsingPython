#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/plus-one/
# Difficulty: Easy 
# Tags: Array, Math

"""
Question 66:
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        s = str(int("".join(map(str, digits)))+1)
        return [int(char) for char in s]