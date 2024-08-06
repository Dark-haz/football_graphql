from Models.PlayerModels.Player import Player
from Models.PlayerModels.PlayerType import PlayerType
from automapper import mapper

#TODO instead of functions , make a config file its cleaner

class Message_Broker:
    
    def player_to_playerType(self , player:Player):
        return mapper.to(PlayerType).map(player)
    
    def playerArr_to_playerTypearr(self , players : list[Player]) :
        return [self.player_to_playerType(player) for player in players]
    
