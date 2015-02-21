#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/add-binary/
# Difficulty: Easy 
# Tags: Math, String

"""
Question 67:
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2))[2:]