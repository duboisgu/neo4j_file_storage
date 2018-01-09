FROM alpine

RUN apt-get update && apt-get install git python3 python3-pip -y
RUN pip3 install requests argparse

RUN git clone https://github.com/duboisgu/neo4j_file_storage.git neo4j
WORKDIR neo4j
CMD make load user=neo4j password=neo4j1
