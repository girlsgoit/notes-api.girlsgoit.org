from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
def index(request):
    return HttpResponse('Hello Git')











@api_view(["GET"])
def note_details(request, note_id):
    note = get_object_or_404(Note, pk = note_id)

    if request.method == "GET":
        serialized_note = NoteSerializer(note)
        return Response(serialized_note.data)