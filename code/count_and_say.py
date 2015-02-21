#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/count-and-say/
# Difficulty: Easy 
# Tags: String

"""
Question 38:
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

"""method 1: normal"""
class Solution:
    # @return a string
    def countAndSay(self, n):
        value = '1'
        #'int' has no 'len()', 'len(n'=integer is not iterable
        for i in xrange(n-1):
            count = 0
            candidate = value[0]
            next = ''
            for index, item in enumerate(value): 
                if item == candidate:
                    count += 1
                else:
                    next += str(count) + candidate
                    count = 1
                    candidate = item
                if index == len(value)-1:
                    next += str(count) + candidate
            value = next
        return value


"""method 2: use itertools module """
class Solution:
    # @return a string
    def countAndSay(self, n):
        value = '1'
        for i in xrange(n-1):
            next = ''
            for item in [list(g) for k,g in itertools.groupby(value)]:
                next += str(len(item)) + item[0]
            value = next
        return value
            


"""method 3: regular expression """
class Solution:
    # @return a string
    def countAndSay(self,n):
        p = re.compile(r'(.)\1*')
        now = '1'
        for i in xrange(n-1):
            prev = now
            now = "".join( iter(  str(m.end()-m.start())+prev[m.start()] for m in re.finditer(p, prev)  ))
        return now   
