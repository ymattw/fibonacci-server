[![Build Status](https://travis-ci.org/ymattw/fibonacci-server.svg?branch=master)](https://travis-ci.org/ymattw/fibonacci-server)

_Just a toy project for demo purpose._

# About

**Fibonacci Server** is a RESTful web service that provides the [Fibonacci
number](https://en.wikipedia.org/wiki/Fibonacci_number) for any given integer
less than a predefined number (default TODO).  Here we assume the sequence
**starts from zero**.

# Requirements

Fibonacci Server requires

- Python >= 2.6 (should already present on modern OS X and Linux distributions)
- [Flask](http://flask.pocoo.org/) web framework, which you can install with
  [pip](https://pip.pypa.io/en/stable/)

In general, you just need to bootstrap pip if you don't have that available on
your system and use it to install Flask.  Here's how:

```bash
which pip || curl -fsSL https://bootstrap.pypa.io/get-pip.py | sudo python
sudo pip install flask
```

If you prefer to install as non-root user, consider use
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

# Run

Just clone the source code, enter the directory and run:

```bash
./fibonacci.py &
```

This will run the service and listen on port `8080` (use option `-p|--port N`
to change the default port). Now the service is running and ready to serve.

# Request

The request format is `GET /:version/fib/:number`, where

- `:version` is the API version, currently only `v1` is implemented
- `:number` is a non-negative integer represents the **first `number` numbers**
  of the Fibonacci sequence

For example:

```bash
curl -is localhost:8080/v1/fib/5
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

# Notes

Although this project is admittedly trivial, imagine we'll have to put into
production and maintain for 5 years, so keep following practices in mind:

Focus on core features first

- [ ] The algorithm
- [ ] The web service
- [ ] Command line option
- [ ] Performance
- [ ] Logging

Follow engineering best practices as we go

- [ ] Implement code lint check (pep8)
- [ ] Implement unit tests and coverage report
- [ ] Implement functional tests
- [ ] Integrate with travis, make sure changes do not break existing logic
- [ ] Iterate the work, each with a short living git branch

Long term (TODO)

- [ ] Start/stop scripts
- [ ] Auto boot
- [ ] Monitoring mechanism
- [ ] Logging to file
- [ ] Log rotate
- [ ] Distributed version
- [ ] Performance for distributed version: caching, pre-computing
