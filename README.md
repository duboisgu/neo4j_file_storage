# Football Grapher

## Requirements
Python3 is needed to easily load the dataset into neo4j's database.

__Debian__ and __Ubuntu__:
```sh
sudo apt-get update && sudo apt-get install python3 pyton3-pip
```

__macOS__ using [HomeBrew](https://brew.sh/):
```sh
brew update && brew install python3
```

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
