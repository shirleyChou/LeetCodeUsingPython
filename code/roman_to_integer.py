#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/roman-to-integer/
# Difficulty: Easy 
# Tags: Math, String

"""
Question 13:
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution:
    # @return an integer
    def romanToInt(self, s):
        d = {'I':lambda i: -1 if s[i+1] in ['V', 'X'] else 1, 
             'X':lambda i: -10 if s[i+1] in ['L', 'C'] else 10,
             'C':lambda i: -100 if s[i+1] in ['D', 'M'] else 100, 
             'V':lambda i: 5, 
             'L':lambda i: 50, 
             'D':lambda i: 500, 
             'M':lambda i: 1000}
        total = 0
        s += '!'
        for i, char in enumerate(s[:-1]):
            total += d[char](i)
        return total
