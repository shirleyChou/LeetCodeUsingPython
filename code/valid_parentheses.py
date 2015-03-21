#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/plus-one/
# Difficulty: Easy 
# Tags: Stack, String

"""
Question 20:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    # @return a boolean
    def isValid(self, s): 
        # string & stack O(n)
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            elif stack == [] or '([{'.index(stack.pop()) != ')]}'.index(char):
                return False
        return stack == [] 
        # not concise enough
        # if len(stack) == 0: return True 
        # else: return False


class Solution:
    # @return a boolean
    def isValid(self, s):
        l = []
        d = {')':'(', '}':'{', ']':'['}
        if s[0] in d.keys():
            return False
        else:
            for char in s:
                if char in d.values():
                    l.append(char)
                elif char in d.keys():
                    if l == [] or l.pop() != d[char]:
                        return False
            return l == []
