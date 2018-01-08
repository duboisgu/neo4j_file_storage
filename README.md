# Football Grapher

## Requirements
In order to automatically load the dataset, `python3` is required with the library
[requests](http://docs.python-requests.org/en/master/)

To check if all the requierements are correctly installed, run:
```sh
make check-requirements
```

## Usage
### Load dataset
In order to load the dataset, please run the following command:
```sh
make load --user=<neo4j_username> --password=<neo4j_password>
```

### Clean database
To drop the loaded data, run:
```sh
make clean --user=<neo4j_username> --password=<neo4j_password>
```
