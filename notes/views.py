from django.http import HttpResponse
from .models import Note, NoteElement, GGITUser
from .serializers import NoteSerializer, NoteElementSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse('Hello Git')

@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        list_of_notes = Note.objects.all()
        serializer_notes = NoteSerializer(list_of_notes, many=True)
        return Response(serializer_notes.data)
    elif request.method == "POST":       
        new_data = request.data
        note_serializer = NoteSerializer(data=new_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        else:
            return Response(note_serialized.errors)


@api_view(["GET"])
def note_details(request, note_id):
    note = get_object_or_404(Note, pk = note_id)

    if request.method == "GET":
        serialized_note = NoteSerializer(note)
        return Response(serialized_note.data)

@api_view(['GET'])
def users(request):
   list_of_users = GGITUser.objects.all()
   serializer_list_of_users = UserSerializer(list_of_users, many = True)
   return Response(serializer_list_of_users.data)
    

@api_view(['GET'])
def note_elements_list(request):
     if request.method == 'GET':
        list_of_elements = NoteElement.objects.all()
        serializer_elements = NoteElementSerializer(list_of_elements, many=True)
        return Response(serializer_elements.data)   
