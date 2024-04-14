all: init test run

run:
	python3 -m src.main

init:
	python3 -m pip install -r requirements.txt

test:
	python3 -m unittest discover -s tests -p "*_test.py"


