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


try:
    xrange
except NameError:
    xrange = range


def singleton(cls):
    """A singleton decorator for classes"""
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Fibonacci(object):

    def __init__(self):
        self._results = [0, 1]

    def generate(self, n):
        """Returns a python `generator` represents the first n numbers in the
        Fibonacci sequence (starts from 0).  Python generator is more efficient
        for iteration.
        """
        for i in xrange(len(self._results), n):
            self._results.append(self._results[i-1] + self._results[i-2])

        for i in xrange(n):
            yield self._results[i]


if __name__ == '__main__':  # pragma: no cover
    import sys

    # Act as a simple command line tool to see how large the sequence is.
    #
    #   python fibonacci.py 100 | wc -c    => 1259
    #   python fibonacci.py 1000 | wc -c   => 107450 (107K)
    #   python fibonacci.py 10000 | wc -c  => 10479753 (10M)
    #   python fibonacci.py 100000 | wc -c => 1045242714 (996M)
    #
    # Limit the number to <= 10000 will be reasonable.
    #
    g = Fibonacci().generate(int(sys.argv[1]))
    print(list(g))
