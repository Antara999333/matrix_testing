
# IDS-706_Proj2
[![CI](https://github.com/Antara999333/Individual-project/actions/workflows/cicd.yml/badge.svg)](https://github.com/Antara999333/Individual-project/actions/workflows/cicd.yml)

[![Format](https://github.com/Antara999333/Individual-project/actions/workflows/format.yml/badge.svg)](https://github.com/Antara999333/Individual-project/actions/workflows/format.yml)

[![OnInstall](https://github.com/Antara999333/Individual-project/actions/workflows/install.yml/badge.svg)](https://github.com/Antara999333/Individual-project/actions/workflows/install.yml)

[![Test](https://github.com/Antara999333/Individual-project/actions/workflows/test.yml/badge.svg)](https://github.com/Antara999333/Individual-project/actions/workflows/test.yml)

# This is my Individual Project 1. . 

##Jupyter Notebook :

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
Test Files:

test_script.py (tests/test_script_descriptive_stats.py): This file contains tests specifically for the Python script.
test_lib.py (tests/test_lib.py): Includes tests for the shared library.
Pinned Requirements File (requirements.txt):

## The requirements.txt file specifies exact versions of project dependencies to ensure consistency and reproducibility.

This project structure is designed to provide organization, maintainability, and ease of testing and validation for the descriptive statistics code implemented in both the Jupyter notebook and the Python script. The Makefile commands automate common development tasks, and the inclusion of test files ensures code reliability.
![Image Alt Text](https://github.com/Antara999333/IDS-706_Proj2/blob/main/desc_stats.png?raw=true)
![Image Alt Text](https://github.com/Antara999333/IDS-706_Proj2/blob/main/MIni%20proj%202%20image.png?raw=true)





