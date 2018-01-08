LOAD CSV WITH HEADERS FROM "~/Téléchargement/teams.csv" AS line
CREATE (:Team {country: line.country, nickname: line.nickname});

LOAD CSV WITH HEADERS FROM "~/Téléchargement/confederations.csv" AS line
CREATE (c:Confederation {name: line.name, continent: line.continent})
MATCH (t:Team {country: line.team})
CREATE (t)-[BELONGS_TO]->(c);


LOAD CSV WITH HEADERS FROM "~/Téléchargement/world_cups.csv" AS line
CREATE (wc:Tournament {name:"World_Championship"})
MATCH (t:team {country: line.winner})
CREATE (t)-[WON {in: line.date, at: line.country}]->(wc);

LOAD CSV WITH HEADERS FROM "~/Téléchargement/olympic_games.csv" AS line
CREATE (og:Tournament {name:"Olympic_Games"})
MATCH (t:team {country: line.winner})
CREATE (t)-[WON {in: line.date, at: line.city}]->(og);

LOAD CSV WITH HEADERS FROM "~/Téléchargement/managers.csv" AS line
CREATE (m:Manager {name: line.manager})
MATCH (t:team {country: line.team})
CREATE (m)-[MANAGE {since: line.since}]->(t);

LOAD CSV WITH HEADERS FROM "~/Téléchargement/captains.csv" AS line
CREATE (c:Captain {name: line.captain})
MATCH (t:team {country: line.team})
CREATE (c)-[PLAY_IN]->(t);

