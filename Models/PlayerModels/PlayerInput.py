import graphene

class PlayerInput(graphene.InputObjectType):
    fn = graphene.String(required=True)
    ln = graphene.String(required=True)
    apt = graphene.Int(required=True)
    set = graphene.Int(required=True)
    position = graphene.String(required=True)
    nationality = graphene.String(required=True)
