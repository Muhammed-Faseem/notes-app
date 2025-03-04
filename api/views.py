import uuid  # Import the uuid module
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .dynamodb_service import DynamoDBService

# Initialize DynamoDBService
dynamodb_service = DynamoDBService(table_name='Note')

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = dynamodb_service.list_items()
    return Response(notes)

@api_view(['GET'])
def getNote(request, pk):
    note = dynamodb_service.get_item({'id': pk})
    return Response(note)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    response = dynamodb_service.put_item({'id': pk, 'body': data['body']})
    return Response(response)

@api_view(['DELETE'])
def deleteNote(request, pk):
    response = dynamodb_service.delete_item({'id': pk})
    return Response(response)

@api_view(['POST'])
def createNote(request):
    data = request.data
    # Generate a unique ID for the new note
    note_id = str(uuid.uuid4())
    response = dynamodb_service.put_item({'id': note_id, 'body': data['body']})
    return Response(response)