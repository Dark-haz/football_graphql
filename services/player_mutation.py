import graphene
from Models.PlayerModels.PlayerInput import PlayerInput
from Models.PlayerModels.PlayerType import PlayerType
from Models.PlayerModels.Player import Player
from Repository.PlayerRepository import PlayerRepository
from services.message_broker import Message_Broker

class CreatePlayer(graphene.Mutation):

    # Define the arguments the mutation will take
    class Arguments:
        player_data = PlayerInput(required=True)
    
    # Define the field that the mutation will return
    player = graphene.Field(lambda: PlayerType)

    def mutate(self, info, player_data):
        _playerDB = PlayerRepository()
        _mbroker = Message_Broker()
        # Use the input data to create a new PlayerType instance
        player = Player(
            fn=player_data.fn,
            ln=player_data.ln,
            apt=player_data.apt,
            set=player_data.set,
            position=player_data.position,
            nationality=player_data.nationality
        )
        # Here you can add logic to save the player to a database if needed.
        _playerDB.add_player(player)
        return CreatePlayer(player= _mbroker.player_to_playerType(player))
