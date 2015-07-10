#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy
# Tags: Hash Table

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true."""


"""method one """
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        return map(s.find, s) == map(t.find, t)


""" method two """
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        return [s.find(i) for i in s] == [t.find(i) for i in t]


"""method three: hash table"""
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        def half_isomorphic(s, t):
            d = {}
            for i, char in enumerate(s):
                if char not in d:
                    d[char] = t[i]
                else:
                    if d[char] != t[i]:
                        return False
            return True
        return half_isomorphic(s, t) and half_isomorphic(t, s)
