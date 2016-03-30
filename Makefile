.PHONY: test lint report-html clean

test: lint
	coverage run --omit='*venv/*' fibonacci_server_test.py
	coverage report --show-missing

lint:
	pep8 *.py

report-html:
	coverage html
	python -m webbrowser -n "file://$(shell pwd)/htmlcov/index.html"

clean:
	rm -rf *.pyc .coverage htmlcov/
