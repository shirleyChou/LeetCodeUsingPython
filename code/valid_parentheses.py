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
        stack = []
        dict = {']':'[','}':'{',')':'('}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or stack.pop() != dict[char]:
                    return False
        return stack == []