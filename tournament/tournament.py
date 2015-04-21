#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM Matches;")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM Players;")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered.

    Returns:
        A single numeric value representing the number of players.
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(Players.id) FROM Players;")
    dat = c.fetchall()
    return dat[0][0]
    DB.close()


def registerPlayer(name):
    """Adds a player to the tournament database.

    Args:
        name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    # Sicures the database from script injection attacks
    user_imput = bleach.clean(name)
    # Sicure the database from sql injection attacks    
    c.execute("INSERT INTO Players (name) VALUES (%s);", (user_imput,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM standings;")
    return c.fetchall()
    DB.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    win = int(winner)
    los = int (loser) 
    c.execute("INSERT INTO Matches (p1, p2, winner) VALUES (%d, %d, %d);"
     % (win, los, win))
    DB.commit()
    DB.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT id, name FROM standings;")
    dat = c.fetchall()
    L = []
    i = 0
    while i < len(dat):
        L.append(dat[i]+dat[i+1])  # Performs concatenation and appends to L
        i = i+2
    return L
    DB.close()




