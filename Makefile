install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	#force install latest whisper
	pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py
