# Python Package Template

## Usage

Use one of the following options to use the template.

* Use this template as described [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template).
* Clone this template `git clone https://github.com/chryb/python-package-template.git` and remove git within the dictionary `rm -rf .git`.

## Install Dependencies

1. Install **Python3** and **pip3**
2. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
3. (Update) To update conda run `conda update conda`

### After Checkout

Run this command to create the environment:

```bash
conda env create -f environment.yml --prefix ./env
```

### Activate/Deactivate

To activate the created environment:

```bash
conda activate ./env
```

To deactivate the actual environment:

```bash
conda deactivate
```

To list all conda environments:

```bash
conda env list
# or
conda info --envs
```

To remove the environment just remove the `.env` dictionary.