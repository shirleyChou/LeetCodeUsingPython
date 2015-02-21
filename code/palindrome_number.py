#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/palindrome-number/
# Difficulty: Easy 
# Tags: Math

"""
Question 9:
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]