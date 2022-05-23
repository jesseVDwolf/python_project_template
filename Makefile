all: install lint test format

install:
	. .venv/bin/activate; pip install --upgrade pip \
		&& pip install -r requirements.txt


test:
	. .venv/bin/activate; python -m pytest -vv test_squared.py

format:
	. .venv/bin/activate; black *.py

lint:
	. .venv/bin/activate; pylint --disable=R,C squared.py

hook: format lint test
