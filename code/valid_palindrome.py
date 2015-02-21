#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/valid-palindrome/
# Difficulty: Easy 
# Tags: Two Pointers, String

"""
Question 125:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

""" method 1: 161 ms"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        for char in s:
            if not char.isalnum():
                s = s.replace(char,"")
        return s.lower() == s.lower()[::-1]


""" method 2: list comprehension 79 ms"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = "".join([char.lower() for char in s if char.isalnum()])
        return s == s[::-1]
        