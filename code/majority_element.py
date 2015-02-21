#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/majority-element/
# Difficulty: Easy 
# Tags: Divide and Conquer, Array, Bit Manipulation

"""
Question 169:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

""" method 1 hash table O(n) """
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        hash = {}
        for value in num:
            if value not in hash.keys():
                hash[value] = 1
            else:
                hash[value] += 1
            if hash[value] > len(num) // 2:
                return value


				
""" method 2 Majority Vote Algorithm/Moore’s Voting Algorithm O(n) """
""" 
http://blog.csdn.net/pi9nc/article/details/9355293 
http://www.cs.utexas.edu/~moore/best-ideas/mjrty/example.html#step13
""" 
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):  
        count = 0
        candidate = num[0]
        for index in xrange(len(num)):
            if num[index] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num[index+1]
        return candidate