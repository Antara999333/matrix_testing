install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black src/*.py
	nbqa black src/*.ipynb 
	

 
	

lint:	
	nbqa ruff *.py  
	nbqa ruff *.ipynb
	
