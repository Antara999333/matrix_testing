install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
        black .  # Format all Python files in the current directory and subdirectories
        nbqa black .ipynb  # Format all Jupyter notebooks in the current directory and subdirectories
 
	

lint:
	nbqa ruff *.py  
	nbqa ruff *.ipynb
