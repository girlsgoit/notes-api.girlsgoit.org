from rest_framework.serializers import ModelSerializer
from .models import Note, NoteElement
from .models import GGITUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        fields = '__all__'


class NoteSerializer(ModelSerializer): 
    class Meta: 
        model = Note
        fields = '__all__'

class NoteElementSerializer(ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'





