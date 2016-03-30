#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fibonacci import Fibonacci


class SingletonTest(unittest.TestCase):

    def test_id(self):
        fib1 = Fibonacci()
        fib2 = Fibonacci()
        self.assertEqual(id(fib1), id(fib2))


class FibonacciTest(unittest.TestCase):

    def setUp(self):
        self._fib = Fibonacci()

    def test_minimal(self):
        self.assertEqual(list(self._fib.generate(0)), [])
        self.assertEqual(list(self._fib.generate(1)), [0])
        self.assertEqual(list(self._fib.generate(2)), [0, 1])

    def test_normal(self):
        self.assertEqual(list(self._fib.generate(6)), [0, 1, 1, 2, 3, 5])

    def test_large(self):
        x = list(self._fib.generate(100))
        self.assertEqual(len(x), 100)
        self.assertEqual(x[97], 83621143489848422977)
        self.assertEqual(x[98], 135301852344706746049)
        self.assertEqual(x[99], 218922995834555169026)

    def test_xlarge(self):
        """Result is too long so just verify the first and last 32 digits of
        the last number
        """
        x = list(self._fib.generate(100000))
        self.assertEqual(len(x), 100000)
        s = str(x[99999])
        self.assertEqual(len(s), 20899)
        self.assertEqual(s[:32], '16052857682729819697035016991663')
        self.assertEqual(s[-32:], '35545120747688390605016278790626')


if __name__ == '__main__':
    unittest.main()
