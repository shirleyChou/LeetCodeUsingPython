#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy 
# Tags: Hash Table, Sort

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        return sorted(list(s)) == sorted(list(t))
