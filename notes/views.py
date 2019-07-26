from django.http import HttpResponse
from .models import Note, GGITUser
from .serializers import NoteSerializer
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

@api_view(['POST'])
def username_is_unique(request):
    if GGITUser.objects.filter(username=request.data['username']).exists():
        return Response(status=400)
    else:
        return Response(status=200)
        