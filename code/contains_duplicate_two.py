#!/usr/bin/env python
# encoding: utf-8

# https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Tags: array, hash table

"""
Question 219:
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for index, value in enumerate(nums):
            if value in d and index - d[value] <= k:
                return True
            else:
                d[value] = index
        return False
