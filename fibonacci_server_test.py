#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test the FibonacciServer module
"""

import unittest
from fibonacci_server import FibonacciServer


class FibonacciServerTest(unittest.TestCase):

    def setUp(self):
        self._app = FibonacciServer()._test_client()

    def test_fib_invalid_version(self):
        rv = self._app.get('/v2/fib/0')
        self.assertTrue(rv.status.startswith('501 '))

    def test_fib_not_a_number(self):
        rv = self._app.get('/v1/fib/xxx')
        self.assertTrue(rv.status.startswith('400 '))

    def test_fib_float_number(self):
        rv = self._app.get('/v1/fib/1.0')
        self.assertTrue(rv.status.startswith('400 '))

    def test_fib_negative_numer(self):
        rv = self._app.get('/v1/fib/-1')
        self.assertTrue(rv.status.startswith('400 '))

    def test_fib_overflowed_number(self):
        rv = self._app.get('/v1/fib/99999999999999')
        self.assertTrue(rv.status.startswith('413 '))

    def test_fib_zero(self):
        rv = self._app.get('/v1/fib/0')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.data, b'[]')

    def test_fib_normal(self):
        rv = self._app.get('/v1/fib/2')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.headers['content-type'], 'application/json')
        self.assertEqual(rv.data, b'[0, 1]')


if __name__ == '__main__':
    unittest.main()
