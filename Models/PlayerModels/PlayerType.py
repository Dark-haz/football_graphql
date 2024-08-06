from graphene import ObjectType 
import graphene

class PlayerType(ObjectType): 
    ID = graphene.ID()
    fn = graphene.String()
    ln = graphene.String()
    apt = graphene.Int()
    set = graphene.Int()
    position = graphene.String()
    nationality = graphene.String()
    avg = graphene.Float()

