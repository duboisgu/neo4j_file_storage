import requests
import argparse
import collections

cypher_requests = collections.OrderedDict()
cypher_requests = [
    ("Teams", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/teams.csv" AS line
    CREATE (:Team {country: line.name, nickname: line.nickname});
    """),

    ("Confederations", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/confederations.csv" AS line
    MATCH (t:Team {country: line.team})
    MERGE (c:Confederation {name: line.name, continent: line.continent})
    CREATE (t)-[:BELONGS_TO]->(c);
    """),

    ("Tournaments objects", """
    CREATE (Tournament1:Tournament {name:"World Championship"})
    CREATE (Tournament2:Tournament {name:"Olympic Games"});
    """),

    ("World Cups", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/world_cups.csv" AS line
    MATCH (wc:Tournament {name: "World Championship"})
    MATCH (t:Team {country: line.winner})
    CREATE (t)-[:WON {in: line.date, at: line.country}]->(wc);
    """),

    ("Olympic Games", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/olympic_games.csv" AS line
    MATCH (og:Tournament {name: "Olympic Games"})
    MATCH (t:Team {country: line.winner})
    CREATE (t)-[:WON {in: line.date, at: line.city}]->(og);
    """),

    ("Managers", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/managers.csv" AS line
    MATCH (t:Team {country: line.team})
    CREATE (m:Manager {name: line.manager})
    CREATE (m)-[:MANAGE {since: line.since}]->(t);
    """),

    ("Captains", """
    LOAD CSV WITH HEADERS FROM "https://raw.githubusercontent.com/duboisgu/neo4j_file_storage/master/CSV/captains.csv" AS line
    MATCH (t:Team {country: line.team})
    CREATE (c:Captain {name: line.captain})
    CREATE (c)-[:PLAY_IN]->(t);
    """)
]


def post_request(target, auth, request):
    r = requests.post(target, auth=auth, data={"query": request})
    assert(r.status_code == 200)


def clean(target, auth):
    print("Cleaning database")
    post_request(target, auth, "match (n) detach delete n;")


def load(target, auth):
    for r in cypher_requests:
        print("Loading: " + r[0])
        post_request(target, auth, r[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    parser.add_argument('--load', action='store_true')
    parser.add_argument('--user', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()

    target = "http://127.0.0.1:7474/db/data/cypher"
    auth = (args.user, args.password)

    if args.clean:
        clean(target, auth)
    elif args.load:
        load(target, auth)


main()
