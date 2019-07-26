from rest_framework.serializers import ModelSerializer
from .models import Note, NoteElement
from .models import GGITUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        fields = '__all__'

class NoteElementSerializer(ModelSerializer):
    class Meta:
        model = NoteElement
        fields = '__all__'

class NoteSerializer(ModelSerializer):
    note_elements = NoteElementSerializer(many=True) 
    class Meta: 
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        notes_data = validated_data.pop('note_elements')
        note = Note.objects.create(user=validated_data['user'], created_at = validated_data['created_at'])
        for note_data in notes_data:
            NoteElement.objects.create(note=note, tag = note_data['tag'], content = note_data['content'])
        return note


