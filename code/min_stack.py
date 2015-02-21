#!/usr/bin/env python
# encoding: utf-8

# https://oj.leetcode.com/problems/min-stack/
# Difficulty: Easy 
# Tags: Stack, Data Structure

"""
Question 155:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = None
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.mini:
            if self.mini > x:
                self.mini = x
        else:
            self.mini = x
        return x

    # @return nothing
    def pop(self):
        top = self.stack.pop()
        if top == self.mini:
            if self.stack:
                self.mini = min(self.stack)
            else:
                self.mini = None
        

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mini