# Python project template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit.com/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit.com/main)

Template for building out a python project using the [poetry](https://python-poetry.org/) build
system, [pytest](https://docs.pytest.org/en/7.1.x/) for testing, [black](https://black.readthedocs.io/en/stable/) for code formatting and [pylint](https://pylint.pycqa.org/en/latest/) for linting. The template also provides a Makefile containing `install`, `test`, `format` and `lint` rules that automatically install the required packages, test the code, format the .py files and lint the .py files.

## poetry
For poetry, a pyproject.toml file is added with the basic dependencies as specified above and [jupyterlab](https://jupyter.org/) as an added --dev dependency since I personally use it so much. A **requirements.txt** file is also added since it's still used for most systems.

## pre-commit
[pre-commit](https://pre-commit.com/) is used to run the Makefile automatically on each commit. The **.pre-commit-config.yaml** file provides some default configuration to get started.

## Makefile
The Makefile will assume that there is a python virtual environment installed next to the Makefile in the folder <kbd>.venv</kbd>. You can use the makefile in the following fashion:

```bash
# run all the rules
make

# install only the packages into the virtual environment using pip
make install

# lint the code
make lint

# format the code using black
make format

# test the code using pytest
make test
```
