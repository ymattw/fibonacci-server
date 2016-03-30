#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Fibonacci sequence (starts from 0) generator.

Usage:
>>> from fibonacci import Fibonacci
>>> f = Fibonacci()
>>> g = f.generate(5)
>>> list(g)
[0, 1, 1, 2, 3]
"""

__all__ = ['Fibonacci']


class Fibonacci(object):

    def __init__(self):
        self._results = [0, 1]

    def generate(self, n):
        """Returns a python `generator` represents the first n numbers in the
        Fibonacci sequence (starts from 0).  Python generator is more efficient
        for iteration.
        """
        if n > 0:
            yield 0
            yield 1
