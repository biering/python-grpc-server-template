init:
	conda env create -f environment.yml --prefix ./env

activate:
	conda activate ./env

deactivate:
	conda deactivate

test:
	py.test tests
