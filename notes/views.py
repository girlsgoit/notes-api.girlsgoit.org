from django.http import HttpResponse
from .models import Note, NoteElement
from .serializers import NoteSerializer, NoteElementSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse('Hello Git')

@api_view(['GET'])
def note_list(request):
    if request.method == 'GET':
        list_of_notes = Note.objects.all()
        serializer_notes = NoteSerializer(list_of_notes, many=True)
        return Response(serializer_notes.data)

@api_view(['GET'])
def note_elements_list(request):
     if request.method == 'GET':
        list_of_elements = NoteElement.objects.all()
        serializer_elements = NoteElementSerializer(list_of_elements, many=True)
        return Response(serializer_elements.data)   
