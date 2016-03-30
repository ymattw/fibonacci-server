#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A RESTful web service that provides the Fibonacci number (starts from 0) for
any given integer less than a predefined number (default TODO)
"""

import json
from flask import Flask, Response
from fibonacci import Fibonacci


class FibonacciServer(object):

    MAX_ACCEPTABLE_NUMBER = 1024  # FIXME: max number TBD

    def __init__(self, host='127.0.0.1', port=8080):
        self._host = host
        self._port = port
        self._app = Flask(__name__)
        self._fib = Fibonacci()
        self._add_routes()

    def fib(self, version, number):
        """Handles the `GET /:version/fib/:number` request. Status goes to
        header, data goes to body in JSON.

        Status codes are:
            - 200 OK
            - 400 BAD REQUEST (invalid parameter)
            - 403 REQUEST ENTITY TOO LARGE (input number too large)
            - 500 INTERNAL SERVER ERROR (unknown exception)
            - 501 NOT IMPLEMENTED (not supported API)
        """
        if version != 'v1':
            return self._response(501)
        try:
            n = int(number)
        except ValueError:
            return self._response(400)
        if n < 0:
            return self._response(400)
        elif n > self.MAX_ACCEPTABLE_NUMBER:
            return self._response(413)

        try:
            seq = list(self._fib.generate(n))
            return self._response(200, seq)
        except:
            return self._response(500)

    def run(self):
        self._app.run(host=self._host, port=self._port)

    def _add_routes(self):
        self._app.add_url_rule(
            '/<version>/fib/<number>', endpoint='fib', view_func=self.fib)

    def _response(self, status, data=None):
        data = data or []
        return Response(json.dumps(data), status=status,
                        mimetype='application/json')

    def _test_client(self):
        return self._app.test_client()


if __name__ == '__main__':  # pragma: no cover
    from optparse import OptionParser

    parser = OptionParser(usage='%prog [options]')
    parser.add_option('-p', '--port', type='int', default=8080,
                      help='Listen port, default is 8080')
    parser.add_option('-a', '--address', default='127.0.0.1',
                      help=('Listen address, default is 127.0.0.1, use '
                            '"0.0.0.0" for all'))
    opts, _ = parser.parse_args()

    server = FibonacciServer(host=opts.address, port=opts.port)
    server.run()
