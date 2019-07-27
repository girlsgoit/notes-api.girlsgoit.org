from django.db import models
from django.contrib.auth.models import AbstractUser

class GGITUser(AbstractUser):
    settings = models.TextField(blank=True)
    full_name = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}.  {self.settings} {self.full_name}"  
class Note(models.Model):  
    user = models.ForeignKey(GGITUser, on_delete = models.CASCADE, related_name="notes")
    created_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. Utilizator: {self.user}; Data creării: {self.created_at}; Postare publică: {self.is_published}"

class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete = models.CASCADE, related_name="note_elements")

    def __str__(self):
        return f"{self.id}. Tag: {self.tag}; {self.content}; {self.note}"