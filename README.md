[![Build Status](https://travis-ci.org/ymattw/fibonacci-server.svg?branch=master)](https://travis-ci.org/ymattw/fibonacci-server)

_Just a toy project for demo purpose._

# About

**Fibonacci Server** is a RESTful web service that provides the [Fibonacci
number](https://en.wikipedia.org/wiki/Fibonacci_number) (starts from 0) for any
given integer less than a predefined number (10,000 for now, see
["Performance"](#performance) section below).

# Requirements

Fibonacci Server requires

- Python 2.6+, 3.3+ or pypy (verified on are 2.6, 2.7, 3.3, 3.4, 3.5 and pypy)
- [Flask](http://flask.pocoo.org/) web framework, which you can install with
  [pip](https://pip.pypa.io/en/stable/)

In general, you just need to bootstrap pip if you don't have that available on
your system and use it to install Flask.  Here's how:

```
$ which pip || curl -fsSL https://bootstrap.pypa.io/get-pip.py | sudo python
$ sudo pip install flask
```

If you prefer to install as non-root user, consider use
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

# Run

Just clone the source code, enter the directory and run:

```
$ ./fibonacci_server.py &
```

This will run the service and listen on port `8080` (use option `-p|--port N`
to change the default port). Now the service is running and ready to serve.

Full usage can be shown with option `--help`:

```
$ ./fibonacci_server.py --help
Usage: fibonacci_server.py [options]

Options:
  -h, --help            show this help message and exit
  -p PORT, --port=PORT  Listen port, default is 8080
  -a ADDRESS, --address=ADDRESS
                        Listen address, default is 127.0.0.1, use "0.0.0.0"
                        for all
```

# Request

The request format is `GET /:version/fib/:number`, where

- `:version` is the API version, currently only `v1` is implemented
- `:number` is a non-negative integer represents the **first `number` numbers**
  of the Fibonacci sequence

For example:

```
$ curl -is localhost:8080/v1/fib/5
```

This should responds you an JSON blob (array) `[0,1,1,2,3]` in the body as well
as a normal status code `200` in the header.  See more status codes below.

# Response

Response is a status code with human readable message in HTTP header and JSON
array in body text (newline ended).  Note body text might contain unexpected
HTML entities so a client should always check HTTP status code before parsing
the body as JSON.

Status codes are listed below.

| Status Code   | Message                  | Explanation                                       |
| ------------- | ------------------------ | ------------------------------------------------- |
| 200           | OK                       | Success, result json will be in body              |
| 400           | BAD REQUEST              | Input is invalid (not an integer or is negative)  |
| 413           | REQUEST ENTITY TOO LARGE | Given number too large                            |
| 500           | INTERNAL SERVER ERROR    | Unknown error happened on server side (check log) |
| 501           | NOT IMPLEMENTED          | Not supported API version                         |

See also [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

# Performance

Counting 10,000 numbers takes _9ms_, counting 100,000 numbers takes _361ms_,
this was done on a pretty recent MBP with 8G memory and python 2.7.10.

```
$ python fibonacci.py 10000
         20002 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.009    0.009 <string>:1(<module>)
    10001    0.007    0.000    0.008    0.000 fibonacci.py:42(generate)
        1    0.000    0.000    0.000    0.000 {len}
     9998    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

$ python fibonacci.py 100000
         200002 function calls in 0.361 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.008    0.008    0.361    0.361 <string>:1(<module>)
   100001    0.346    0.000    0.353    0.000 fibonacci.py:42(generate)
        1    0.000    0.000    0.000    0.000 {len}
    99998    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

On the other hand, size of response body reaches _10MB_ for _n=10,000_ and
_~1GB_ for _n=100,000_, so limit the `fibonacci_server` to accept a number **<=
10000** would be reasonable in both response time and size.

```
$ python fibonacci.py 100 | wc -c     # 1259
$ python fibonacci.py 1000 | wc -c    # 107450 (107K)
$ python fibonacci.py 10000 | wc -c   # 10479753 (10M)
$ python fibonacci.py 100000 | wc -c  # 1045242714 (996M)
```

# Notes

Although this project is admittedly trivial, imagine we'll have to put into
production and maintain for 5 years, so keep following practices in mind:

Focus on core features first

- [X] The algorithm
- [X] The web service
- [X] Command line option
- [X] Performance
- [ ] Logging

Follow engineering best practices as we go

- [X] Implement code lint check (pep8)
- [X] Implement unit tests and coverage report
- [ ] Implement functional tests
- [X] Integrate with travis, make sure changes do not break existing logic
- [X] Iterate the work, each with a short living git branch

Long term (TODO)

- [ ] Start/stop scripts
- [ ] Auto boot
- [ ] Monitoring mechanism
- [ ] Log rotate
- [ ] Distributed version
- [ ] Performance for distributed version: caching, pre-computing
