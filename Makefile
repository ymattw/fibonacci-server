.PHONY: test lint report-html clean

test: lint
	coverage run --append --omit='*venv/*' fibonacci_test.py
	coverage run --append --omit='*venv/*' fibonacci_server_test.py
	coverage report --show-missing

lint:
	pep8 *.py

# Open the html report in browser
report-html:
	coverage html
	python -m webbrowser -n "file://$(shell pwd)/htmlcov/index.html"

clean:
	rm -rf *.pyc *.log *.log.* .coverage htmlcov/ __pycache__/
