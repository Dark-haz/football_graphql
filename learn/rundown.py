import graphene
from flask import Flask , request , jsonify
from graphene import ObjectType 

app = Flask (__name__)

# Define the Book type 
class BookType(ObjectType): #> graphQL object that can used in queries
     title = graphene.String() 
     author = graphene.String()



# Define the Query class 
#> Defines the root query type. 
# > There can be only ONE root query
#> In GraphQL, queries are used to read or fetch values. 
class Query(ObjectType):
    #> A field in the Query class that returns the object type
    test = graphene.String()
    books = graphene.List (BookType) #allowed query  

    def resolve_test (self , info):
        return "Test is accessed"

    #> resolver method that provides the data for the Query fields
    def resolve_books (self, info): # runs when query is invoked , need to be query resolve_query
        return [
        BookType(title="Book 1", author="Author 1"), 
        BookType(title="Book 2", author="Author 2")
        ]
    
    



schema = graphene.Schema(query=Query)



@app.route('/', methods=['POST'])
def graphql_server():
    data = request.get_json()
    query = data.get('query')

    result = schema.execute(query) ## one schema 

    return jsonify(result.data)


if __name__ == '__main__':
    app.run()