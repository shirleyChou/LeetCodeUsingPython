#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/excel-sheet-column-number/
# Difficulty: Easy 
# Tags: Math

"""
Question 171:
Related to question:https://oj.leetcode.com/problems/excel-sheet-column-title/

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        L = list(s)
        sum = 0
        for i in range(len(L)):
            sum = sum+(26**i)*(ord(L.pop())-64)
        return sum

