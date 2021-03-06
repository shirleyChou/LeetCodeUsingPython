#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/length-of-last-word/
# Difficulty: Easy 
# Tags: String

"""
Question 58:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s):
            if s.split():
                return len(s.split()[-1])
            else:
                return 0
        else:
            return 0