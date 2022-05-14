# Python project template
Template for building out a python project using the [pip](https://pip.pypa.io/en/stable/) build
system, [pytest](https://docs.pytest.org/en/7.1.x/) for testing, [black](https://black.readthedocs.io/en/stable/) for code formatting and [pylint](https://pylint.pycqa.org/en/latest/) for linting. The template also provides a Makefile containing `install`, `test`, `format` and `lint` rules that automatically install the required packages, test the code, format the .py files and lint the .py files.

## Pip
For pip, a **requirements.txt** file is added with the basic dependencies as specified above and [jupyterlab](https://jupyter.org/) as an added development dependency since I personally use it so much.

## pre-commit
[pre-commit](https://pre-commit.com/) is used to run the Makefile automatically on each commit. The **.pre-commit-config.yaml** file provides some default configuration to get started.

## github actions
A very simple github actions **.github/workflows/main.yaml** config file is provided to matrix test the project for python versions 3.8, 3.9 and 3.10.

<kbd>squared.py</kbd> and <kbd>test_squared.py</kbd> are there just for example and should be replaced with project specific files.
