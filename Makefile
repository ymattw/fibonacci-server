.PHONY: test lint unit report-html functional clean

test: lint unit functional
	
lint:
	pep8 *.py

unit:
	coverage erase
	coverage run --append --omit='*/lib*/python*/*' fibonacci_test.py
	coverage run --append --omit='*/lib*/python*/*' fibonacci_server_test.py
	coverage report --show-missing

# Open the html report in browser
report-html:
	coverage html
	python -m webbrowser -n "file://$(shell pwd)/htmlcov/index.html"

functional:
	./test.sh

clean:
	rm -rf *.pyc *.log *.log.* .coverage htmlcov/ __pycache__/
