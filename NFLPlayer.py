
class Player():
    def __init__(self, name, passing_attempt, passing_total, rushing_td, ints, rush_attempts):
        self.__name = name
        self.__passing_attempt = passing_attempt
        self.__passing_total = passing_total
        self.__rushing_td = rushing_td
        self.__ints = ints
        self.__rush_attempts = rush_attempts

    # getters

    def getName(self):
        return self.__name


    def getPassingAttempt(self):
        return self.__passing_attempt


    def getPassingTotal(self):
        return self.__passing_total


    def getRushingTD(self):
        return self.__rushing_td


    def getInts(self):
        return self.__ints


    def getRushAttempts(self):
        return self.__rush_attempts



