

[![CI](https://github.com/Antara999333/matrix_testing/actions/workflows/cicd.yml/badge.svg)](https://github.com/Antara999333/matrix_testing/actions/workflows/cicd.yml)

# This is my Mini Project 4
. 
This project shows how GitHub Actions can be used to create a matrix for running a script with different Python versions
## Jupyter Notebook :

This notebook contains cells that perform descriptive statistics using the Pandas library. It has been validated using the nbval plugin for pytest.

## Python Script :

This script executes the same descriptive statistics using Pandas as the Jupyter notebook.

## Library:

The lib.py file holds shared code that is used by both the Python script and the Jupyter notebook. This allows for code reusability and maintainability.

## Makefile:

The Makefile contains four commands that are executed by GitHub Workflows on each push and pull request:

Test: This command runs all tests, including those for the notebook, script, and library.
Format: It formats the code using Python black, ensuring consistent code style.
Lint: This command lints the code using Ruff to identify and address any code quality issues.
OnInstall: It installs project dependencies by running pip install -r requirements.txt.




 ![Alt Text](mini_4.jpg.png)


![Image Alt Text](https://github.com/Antara999333/IDS-706_Proj2/blob/main/desc_stats.png?raw=true)
![Image Alt Text](https://github.com/Antara999333/IDS-706_Proj2/blob/main/MIni%20proj%202%20image.png?raw=true)





