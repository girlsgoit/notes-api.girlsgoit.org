from django.db import models
from django.contrib.auth.models import AbstractUser

class GGITUser(AbstractUser):
    settings = models.TextField()

class Note(models.Model):  
    user = models.ForeignKey(GGITUser, on_delete = models.CASCADE, related_name="notes")
    created_at = models.DateField()

class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete = models.CASCADE, related_name="note_elements")