from rest_framework.serializers import ModelSerializer
from .models import Note
from .models import GGITUser

class NoteSerializer(ModelSerializer): 
    class Meta: 
        model = Note
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        fields = '__all__'