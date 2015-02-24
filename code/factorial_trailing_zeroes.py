#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/factorial-trailing-zeroes/
# Difficulty: Easy 
# Tags: Math

"""
Question 172:
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
"""

"""
can't use math.factorial(n). Time Limit Exceeded. eg.math.factorial(5900)

so the key point is: 
meet the number that can be dived by 5, the Trailing will have 1 more zero and meet the number that can be dived by 5*5, the Trailing will have 2 more zero...
so we just find how many number can be dived by 5, can be dived by 5*5 ... and sum up.
"""

"""method 1 """
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r
        
""" Method 2: recursion """
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
         return 0 if n < 5 else n/5 + self.trailingZeroes(n/5)
