
# python variable definition
ifeq ($(OS),Windows_NT)
	PYTHON=python
else
	PYTHON=python3
endif

all: init test run

run:
	$(PYTHON) -m src.main

init:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m unittest discover -s tests -p "*_test.py"


