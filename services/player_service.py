from Repository.PlayerRepository import *


class Player_Service:
    def __init__(self) -> None:
        self._playerDB = PlayerRepository()

    #>TASK 1 
    #>TASK 2 in Models>Player.py
    def storePlayers(self , players:list[Player]):
        self._playerDB.add_players(players)


    #> TASK 3
    def selectPositions( self , defendersNum , midfieldersNum , attackersNum) -> list[Player]:
        """
            returns array of players for selected position numbers
        """
        #TODO make performance better by limiting instaed of slicing

        col_values_count = self._playerDB.get_col_values_count("position")

        if(col_values_count == {}) : raise Exception("Empty DB , use /storePlayers endpoint")

        if(col_values_count["defender"]< defendersNum) : raise Exception(f"Defenders num must be <= {col_values_count['defender']}")
        if(col_values_count["midfielder"]< midfieldersNum) : raise Exception(f"Midfielders num must be <= {col_values_count['midfielder']}")
        if(col_values_count["attacker"]< attackersNum) : raise Exception(f"Attackers num must be <= {col_values_count['attacker']}")

        defenders = self._playerDB.getAll("avg" , False , position = "defender")
        attackers = self._playerDB.getAll("avg" , False , position = "attacker")
        midfielders = self._playerDB.getAll("avg" , False , position = "midfielder")
        


        aggregate  = defenders[0:defendersNum] + midfielders[0:midfieldersNum] + attackers[0:attackersNum]
        return aggregate

    #> TASK 4
    def selectRandomPlayers(self , playerNum:int) -> list[Player]:
        """
            returns array containing N random players 
        """
        random_player_array = self._playerDB.get_random_entries(playerNum)

        return random_player_array

    #> TASK 5
    def playersPositionReport(self) -> dict:
        """
            returns dictionary -> field : count
        """
        return self._playerDB.get_col_values_count("position")
    

    #> TASK 6
    def sortByAPT(self) -> list[Player]:
        sorted_player_array = self._playerDB.getAll("apt" , False)
        return sorted_player_array


    #> TASK 7
    def findMaxAPT(self):
        maxAPT =  self._playerDB.get("apt" , False)
        return maxAPT



    #> TASK 8
    def findMinAVG(self):
        minAVG =  self._playerDB.get("avg" , True)
        
        return minAVG
    
    #> TESTING
    def test(self):
        return  self._playerDB.get_col_values_count("position")

    


