import requests
import argparse

cypher_requests = {
    "Teams": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/teams.csv" AS line
    CREATE (:Team {country: line.name, nickname: line.nickname});
    """,

    "Confederations": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/confederations.csv" AS line
    MATCH (t:Team {country: line.team})
    MERGE (c:Confederation {name: line.name, continent: line.continent})
    CREATE (t)-[:BELONGS_TO]->(c);
    """,

    "Tournaments objects": """
    CREATE (Tournament1:Tournament {name:"World Championship"})
    CREATE (Tournament2:Tournament {name:"Olympic Games"});
    """,

    "World Cups": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/world_cups.csv" AS line
    MATCH (wc:Tournament {name: "World Championship"})
    MATCH (t:Team {country: line.winner})
    CREATE (t)-[:WON {in: line.date, at: line.country}]->(wc);
    """,

    "Olympic Games": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/olympic_games.csv" AS line
    MATCH (og:Tournament {name: "Olympic Games"})
    MATCH (t:Team {country: line.winner})
    CREATE (t)-[:WON {in: line.date, at: line.city}]->(og);
    """,

    "Managers": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/managers.csv" AS line
    MATCH (t:Team {country: line.team})
    CREATE (m:Manager {name: line.manager})
    CREATE (m)-[:MANAGE {since: line.since}]->(t);
    """,

    "Captains": """
    LOAD CSV WITH HEADERS FROM "https://github.com/duboisgu/neo4j_file_storage/blob/master/CSV/captains.csv" AS line
    MATCH (t:Team {country: line.team})
    CREATE (c:Captain {name: line.captain})
    CREATE (c)-[:PLAY_IN]->(t);
    """
}


def post_request(target, auth, request):
    r = requests.post(target, auth=auth, data={"query": request})
    assert(r.status_code == 200)


def clean(target, auth):
    print("Cleaning database")
    post_request(target, auth, "match (n) detach delete n;")


def load(target, auth):
    for r in cypher_requests:
        print("Loading: " + r)
        post_request(target, auth, cypher_requests[r])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', action='store_true')
    parser.add_argument('--load', action='store_true')
    parser.add_argument('--username', type=str, required=True)
    parser.add_argument('--password', type=str, required=True)
    args = parser.parse_args()

    target = "http://127.0.0.1:7474/db/data/cypher"
    auth = (args.username, args.password)

    if args.clean:
        clean(target, auth)
    elif args.load:
        load(target, auth)


main()
