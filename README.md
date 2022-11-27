# CP317 PROJECT


# Environment Setup

## 1. Install MiniConda
Follow the installation instructions for your operating system. [Download link](https://docs.conda.io/en/latest/miniconda.html)

## 2. Setup the virtual environment

```bash
conda env create -f env.yml
```

## 3. Run program
```bash
python main.py
```

# Testing

## Unit tests
Run the command below at the root level of the project.
`python3 -m coverage run -m unittest`
This will run all test cases and generate a coverage report.

## Check Test Coverage
Run command `coverage report -m` to get a report on the console. \

To view report as a website with more details run:
```bash
coverage html
python3 -m http.server 5555 --directory ./htmlcov
```

## Run test.py 

# Extras

## Export Environment
```bash
conda env export --from-history | grep -v "^prefix: " > env.yml
```