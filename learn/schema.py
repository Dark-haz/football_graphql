import graphene

# Import the models
from learn.models import Author, Book

# Define the AuthorType and BookType as graphene ObjectTypes
class AuthorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class BookType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.Field(lambda: AuthorType)

    # Resolve the author field using the author_id
    def resolve_author(parent, info):
        return next(author for author in authors if author.id == parent.author_id)

# Sample data
authors = [
    Author(id="1", name="Author 1"),
    Author(id="2", name="Author 2"),
]

books = [
    Book(id="1", title="Book 1", author_id="1"),
    Book(id="2", title="Book 2", author_id="2"),
]

# Define the Query class
class Query(graphene.ObjectType):
    # Define a field to get all books
    all_books = graphene.List(BookType)
    # Define a field to get a book by ID
    book = graphene.Field(BookType, id=graphene.ID())

    # Resolver for all_books
    def resolve_all_books(root, info):
        return books

    # Resolver for book by ID
    def resolve_book(root, info, id):
        return next(book for book in books if book.id == id)

# Create the schema
schema = graphene.Schema(query=Query)
