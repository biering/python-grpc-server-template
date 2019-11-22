# Python Package Template

## Usage

Use one of the following options to use the template:

* Use this template as described [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).
* Clone this template `git clone https://github.com/chryb/python-package-template.git` and remove git within the dictionary `rm -rf .git`.

## Install Dependencies

1. Install **Python3** and **pip3**
2. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
3. (Update) To update conda run `conda update conda`

### Setup Environment

Run this command to create the environment:

```bash
conda env create -f environment.yml --prefix ./env
```

### Activate/Deactivate Environment

To activate the created environment:

```bash
conda activate ./env
```

To deactivate the actual environment:

```bash
conda deactivate
```

### Updating an Environment

To update the environment, all you need to do is update the contents of your `environment.yml` file accordingly and then run the following command:

```bash
conda env update --prefix ./env --file environment.yml  --prune
```

### Discover Environments

To list all conda environments:

```bash
conda env list
# or
conda info --envs
```

### Removing an Environment

To remove the environment just remove the `.env` dictionary.

For more information see the conda [documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Features

Don't forget to start with activating the environment with `conda activate ./env`.

### Linting

Linting the package is powered by **flake8**. Just run `flake8 src/` to lint the project or `flake8 src/file.py` to lint a specific file.

### Testing

Run tests by using [pytest](http://doc.pytest.org/en/latest/contents.html) with `pytest -q tests/test.py`.
