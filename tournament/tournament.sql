-- Table definitions for the tournament project.
--
-- This file SQL contains all 'create database', 'create table' and 'create view'
-- statements if you choose to use it.


-- Creates database.
CREATE DATABASE tournament;


-- Connencts to database.
\c tournament;


-- Creates Players table, which stores:
-- automatically assigned id as primary key and the registered name.
CREATE TABLE Players(
		id	serial PRIMARY KEY,
		name	text
);

-- Creates Matches table, which stores:
-- referenced ids of two opponent players and the referenced id of the winner.
CREATE TABLE Matches(
		match	serial PRIMARY KEY,
		p1	integer REFERENCES Players (id),
		p2	integer REFERENCES Players (id),
		winner	integer REFERENCES Players (id)
);


-- Creates games view, which stores:
-- id of the player and number of total matches played.
-- ordered by player id
CREATE VIEW games AS
	SELECT Players.id, count(p1) AS total FROM Players 
		LEFT JOIN (SELECT Matches.p1 FROM Matches 
		UNION ALL SELECT Matches.p2 FROM Matches) AS foo
	ON Players.id = p1
	GROUP BY Players.id
	ORDER BY Players.id;


-- Creates victories view, which stores:
-- id of the player and number of total wins.
-- ordered by player id
CREATE VIEW victories AS
	SELECT Players.id AS id, count(Matches.winner) AS wins
		FROM Players LEFT JOIN Matches
	ON Matches.winner = Players.id
	GROUP BY id
	ORDER BY id;	


-- Creates standings view, which stores:
-- id of the player, given name, number of played matches and number of wins
-- sorted by highest wins score.
CREATE VIEW Standings AS
	SELECT Players.id, Players.name, victories.wins, games.total
		FROM ((Players JOIN victories
			ON Players.id = victories.id)
		JOIN games
			ON Players.id = games.id)
	ORDER BY victories.wins DESC;


