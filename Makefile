install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black main/*.py
	nbqa black main/*.ipynb 
	
lint:	
	nbqa check main/*.py  
	nbqa ruff main/*.ipynb
	
