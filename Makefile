run:
	venv/bin/python -m app

setup:
	python3.8 -m venv venv
	venv/bin/pip install -r requirements.txt
