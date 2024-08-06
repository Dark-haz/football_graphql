import graphene
from flask import Flask , request , jsonify
from graphene import ObjectType 
from Models.PlayerModels.PlayerType import PlayerType
from services.message_broker import Message_Broker
from services.player_service import Player_Service
from services.player_mutation import CreatePlayer

app = Flask (__name__)

_mbroker = Message_Broker()
_player_service = Player_Service()

#> Data querying
class Query(ObjectType):
    minAVG = graphene.Field(PlayerType )
    positions = graphene.List(PlayerType , de = graphene.Int(required=True) ,mf = graphene.Int(required=True) ,at = graphene.Int(required=True))
    # createPlayers = graphene.Field(PlayerType)

    def resolve_minAVG (self , info):
        return _mbroker.player_to_playerType(_player_service.findMinAVG())
    
    def resolve_positions (self , info , de ,  mf , at):
        return _mbroker.playerArr_to_playerTypearr(_player_service.selectPositions(de , mf , at))
    
#> Data mutation
class Mutation(ObjectType):
    createPlayer = CreatePlayer.Field()
    

schema = graphene.Schema(query=Query , mutation=Mutation)

@app.route('/', methods=['POST'])
def graphql_server():
    data = request.get_json()
    query = data.get('query')

    result = schema.execute(query) 

    return jsonify(result.data)


if __name__ == '__main__':
    app.run()

query = '''
    mutation {
      createPlayer(playerData : {fn: "noo", ln: "Doe", apt: 10, set: 1, position: "Forward", nationality: "American"}) {
        player {
          fn
          ln
          apt
          set
          position
          nationality
        }
        
      }
    }
    '''

print(schema.execute(query))