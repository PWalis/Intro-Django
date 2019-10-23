from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from notes.models import Note, Room_DB

class NoteType(DjangoObjectType):
# NoteType is the class GraphQL will use to get data from the model specified 
    class Meta:
        # which model do we want to export as nodes, it will be our Note class
        # model being the class we want to extract data from
        model = Note
        interface = (graphene.relay.Node,)

class Room_DBType(DjangoObjectType):

    class Meta:
        model = Room_DB
        interface = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    # query will return this NoteType object that is being declared
    # NoteType corrisponds to the Note model(above)
    notes = graphene.List(NoteType)
    rooms = graphene.List(Room_DBType)

    def resolve_notes(self, info):
        # Returns all the Note objects as a set
        return Note.objects.all()

    def resolve_rooms(self, info):
        # Returns all the room objects as a set
        return Room_DB.objects.all()

# This variable gets connected to graphene in the settings.py 
# so that graphene knows that this is a querying interface 
schema = graphene.Schema(query=Query)