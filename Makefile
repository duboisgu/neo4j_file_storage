PYTHON=python3
SCRIPT=./loader.py

load:
	@if [[ -z "$(username)" && -z "$(password)" ]]; then \
	 	echo "Usage: make load --user=<neo4j_username> --password=<neo4j_password>"; \
		exit; \
	fi; \
	$(PYTHON) $(SCRIPT) --load --username $(username) --password $(password);

clean:
	@if [[ -z "$(username)" && -z "$(password)" ]]; then \
	 	echo "Usage: make clean --user=<neo4j_username> --password=<neo4j_password>"; \
		exit; \
	fi; \
	$(PYTHON) $(SCRIPT) --clean --username $(username) --password $(password);

check-requirements:
	@python3 --version > /dev/null 2>&1 || { echo >&2 "Python 3 is not correctly installed."; }
	@if [ -z "$(shell pip3 list | grep requests)" ]; then \
		echo "Package \"requests\" not installed. Run \"pip3 install requests\""; \
	else \
		echo "All requirements are correctly installed."; \
	fi; \
