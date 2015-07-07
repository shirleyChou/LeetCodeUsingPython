#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Tags: array, hash table

"""
Question 217:
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)
