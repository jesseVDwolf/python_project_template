# Python project template
Template for building out a python project using the [poetry](https://python-poetry.org/) build
system, [pytest](https://docs.pytest.org/en/7.1.x/) for testing, [black](https://black.readthedocs.io/en/stable/) for code formatting and [pylint](https://pylint.pycqa.org/en/latest/) for linting. The template also provides a Makefile containing `install`, `test`, `format` and `lint` rules that automatically install the required packages, test the code, format the .py files and lint the .py files.

For poetry, a pyproject.toml file is added with the basic dependencies as specified above and [jupyterlab](https://jupyter.org/) as a added --dev dependency since I personally use it so much. A **requirements.txt** file is also added since it's still used for most systems.

<kbd>squared.py</kbd> and <kbd>test_squared.py</kbd> are there just for example and should be replaced with project specific files.
