# CP317 PROJECT - Student Grades Formatter

![](./docs/images/sgf_ascii_art.png)

# Quick Start

## System Requirements

1. Python 3.9.x or later - [Download](https://www.python.org/downloads/) from official site.

## Installation Steps

### Install using `pip`.

```bash
python3 -m pip install . --use-feature=in-tree-build
```

## Try it out!

Run the command below to start using the program.

```bash
sgf
```

![](./docs/images/sgf_screenshot.png)

# Development Environment Setup

## 1. Install MiniConda

Follow the installation instructions for your operating system. [Download link](https://docs.conda.io/en/latest/miniconda.html)

## 2. Setup the virtual environment

```bash
conda env create -f env.yml
```

# Testing

Run the command below at the root level of the project.

```bash
python3 -m coverage run -m unittest -b
```

This will run all test cases and generate a coverage report.

## Check Test Coverage

View coverage report results.

```bash
coverage report
```

To view report as a website with more details run:

```bash
coverage html
python3 -m http.server 5555 --directory ./htmlcov
```

## Install Package as Command Script

**NOTE**: Only for development environment!

```bash
cd /project/root/directory
pip install . --use-feature=in-tree-build
```

## Alternate way to run tests

Run the `test.py` file in the root level of the project. This option will run the tests but not create a coverage report.

```bash
python3 test.py
```

# Extras

## Export Environment

```bash
conda env export --from-history | grep -v "^prefix: " > env.yml
```
