import graphene

# > MODEL CLASSES
class PersonInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    age = graphene.Int(required=True)

class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


#> MUTATION CLASS

class CreatePerson(graphene.Mutation):
    class Arguments:
        person_data = PersonInput(required=True)

    person = graphene.Field(Person)

    def mutate(root, info, person_data=None):
        person = Person(
            name=person_data.name,
            age=person_data.age
        )
        return CreatePerson(person=person)


#> DEFINE SCHEMA
class Query(graphene.ObjectType):
    person = graphene.Field(Person)

class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field() 


schema = graphene.Schema(query=Query, mutation=MyMutations)


query = '''
mutation myFirstMutation {
    createPerson(name:"Peter") {
        person {
            name
        }
        ok
    }
}
'''

p = schema.execute(query)

print(p)