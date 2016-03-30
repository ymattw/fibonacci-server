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
    import cProfile

    # Act as a simple command line tool and take a number from command line
    try:
        number = int(sys.argv[1])
    except:
        raise SystemExit('Please provide a postive number')

    fib = Fibonacci()
    statement = 'seq = list(fib.generate(number))'

    # Too bad cProfile does not support dumping to stderr.  Here is the trick:
    #
    # a) If stdout is redirected to a file or `wc -c`, just print the results
    # b) Otherwise just dump the profiling data
    #
    if sys.stdout.isatty():
        cProfile.run(statement)
    else:
        exec(statement)
        print(seq)
