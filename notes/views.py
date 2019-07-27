from django.http import HttpResponse
from .models import Note, GGITUser,NoteElement
from .serializers import NoteSerializer, NoteElementSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, render


def index(request):
    return HttpResponse('Hello Git')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def note_list(request):
    if request.method == 'GET':
        list_of_notes = Note.objects.all()
        serializer_notes = NoteSerializer(list_of_notes, many=True)
        return Response(serializer_notes.data)
    elif request.method == "POST":       
        new_data = request.data
        new_data["user"] = request.user.id
        if not new_data.get('note_elements'):
            new_data['note_elements'] = []
        
        note_serializer = NoteSerializer(data=new_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        else:
            return Response(note_serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def username_is_unique(request):
    if GGITUser.objects.filter(username=request.data['username']).exists():
        return Response(status=400)
    else:
        return Response(status=200)
        
@api_view(["GET",'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def note_details(request, note_id):
    note = get_object_or_404(Note, pk = note_id)
    serialized_note = NoteSerializer(note)
    if request.method == "GET":
        return Response(serialized_note.data)
    elif request.method == 'PUT':
        request_data=request.data
        serialized_note = NoteSerializer(note, request_data)    
        if serialized_note.is_valid():
            serialized_note.save()
            return Response(serialized_note.data)
        else:
            return Response(serialized_note.errors)
    else:
        note.delete()
        return Response(status= 200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
   list_of_users = GGITUser.objects.all()
   serializer_list_of_users = UserSerializer(list_of_users, many = True)
   return Response(serializer_list_of_users.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def note_elements_list(request):
     if request.method == 'GET':
        list_of_elements = NoteElement.objects.all()
        serializer_elements = NoteElementSerializer(list_of_elements, many=True)
        return Response(serializer_elements.data)   

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def user_details(request, user_id):
    user = get_object_or_404(GGITUser, pk=user_id)
    if request.method == 'GET':
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)
    elif request.method == 'PUT':
        request_data = request.data
        serialized_user = UserSerializer(user, request_data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)
        else:
            return Response(serialized_user.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def publish_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.is_published =  True
    note.save()
    return Response(status=200)

@api_view(['POST'])
def register(request):
    user_data = request.data
    password = user_data['password']
    register_serialized = UserSerializer(data=user_data)
    if register_serialized.is_valid():
        user_instance = register_serialized.save()
        user_instance.set_password(password)
        user_instance.save()
        return Response(register_serialized.data, status = 201)
    else:
        return Response(register_serialized.errors, status= 406)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_me(request):
    user_data = request.user
    serialized_user_me = UserSerializer(user_data)
    return Response(serialized_user_me.data)