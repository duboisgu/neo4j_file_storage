PYTHON=python3
SCRIPT=./loader.py
SHELL=/bin/bash

load:
	@if [[ -z "$(user)" && -z "$(password)" ]]; then \
	 	echo "Usage: make load --user=<neo4j_user> --password=<neo4j_password>"; \
		exit; \
	fi; \
	$(PYTHON) $(SCRIPT) --load --user $(user) --password $(password);

clean:
	@if [[ -z "$(user)" && -z "$(password)" ]]; then \
	 	echo "Usage: make clean --user=<neo4j_user> --password=<neo4j_password>"; \
		exit; \
	fi; \
	$(PYTHON) $(SCRIPT) --clean --user $(user) --password $(password);

check-requirements:
	@python3 --version > /dev/null 2>&1 || { echo >&2 "Python 3 is not correctly installed."; }
	@pip3 --version > /dev/null 2>&1 || { echo >&2 "pip3 is not correctly installed."; }
	@if [ -z "$(shell pip3 list | grep requests)" ]; then \
		echo "Package \"requests\" not installed. Run \"pip3 install requests\""; \
	fi; \
