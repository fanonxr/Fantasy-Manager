class Team():

    def __init__(self, name):
        self.name = name.lower()
        # a set of dictionaries so there cannot be duplicates
        self.fantasy_team = {}

    def __str__(self):
        return f"{self.name} is a fantasy football team that consists of {self.__fantasy_team}"

    # getters
    def getTeam(self):
        """
        Function that will return the players within the fantasy football team
        """
        return self.fantasy_team


    def addPlayer(self, nfl_player):
        """
        function that will add the players to the given fantasy team

        1. prompt user to locate the player they want to add from the table
        """


    def deletePlayer(self, nfl_player):
        """
        function that will delete the player within that fantasy team

        1. prompt the user to select the player they want to delete
        """













