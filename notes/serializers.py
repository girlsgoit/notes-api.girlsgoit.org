from rest_framework.serializers import ModelSerializer
from .models import Note, NoteElement

class NoteSerializer(ModelSerializer): 
    class Meta: 
        model = Note
        fields = '__all__'







class NoteElementSerializer(ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'
