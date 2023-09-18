install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py
	nbqa black *.ipynb 
	
lint:	
	nbqa check *.py  
	nbqa ruff *.ipynb
	
