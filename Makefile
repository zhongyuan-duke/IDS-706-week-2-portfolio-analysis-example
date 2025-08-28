install:
	pip install -r requirements.txt

format:
	black *.py
	
lint:
	flake8 --ignore=E501,N8,C *.py

test:
	pytest

run:
	python portfolio.py

clean:
	rm -rf __pycache__ *.pyc
	rm -rf .pytest_cache		