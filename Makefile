SHELL=/bin/bash

install:
	conda env create -f environment.yml --prefix ./env

update:
	conda env update --prefix ./env --file environment.yml  --prune

activate:
	conda init bash
	conda activate ./env

deactivate:
	conda deactivate

lint:
	flake8 src/

test:
	pytest -q tests/test.py
