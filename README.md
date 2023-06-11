# test_project

This is an example Python project for demonstration purposes. See [code project management](https://github.com/prestonlab/wiki/wiki/Code-project-management) for details.

## Installation

Create a Python virtual environment:

```bash
python -m venv venv
```

Install the package and scripts:

```bash
pip install -U pip
pip install -e .
```

To set up for use with Jupyter, you must install a kernel:

```bash
python -m ipykernel install --user --name myproject
```

You should see this kernel as an option when you create a new notebook in Jupyter.

## Usage

To print "hello world" using a Python script:

```bash
hello-world
```

To print "hello world" using a Bash script:

```bash
hello-world2
```
