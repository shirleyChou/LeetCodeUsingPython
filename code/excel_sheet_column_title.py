#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/excel-sheet-column-title/
# Difficulty: Easy 
# Tags: Math

"""
Question 168:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""

class Solution:
    # @return a string
    def convertToTitle(self, num):
        stack = []
        while num:
            if num%26 != 0:
                stack.append(chr(num%26+64))
                num = num/26
            else:
                stack.append('Z')
                num = num/26-1
        stack.reverse()
        return ''.join(stack)

 
""" two beautiful answer """
 
"""
 https://oj.leetcode.com/discuss/19139/python-solution-with-explanation
 https://oj.leetcode.com/discuss/19044/share-simple-solution-just-little-trick-handle-corner-case
"""