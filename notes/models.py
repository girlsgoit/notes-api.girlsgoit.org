from django.db import models
from django.contrib.auth.models import AbstractUser

class GGITUser(AbstractUser):
    settings = models.TextField()

class Note(models.Model):  
    user = models.ForeignKey(GGITUser, on_delete = models.CASCADE, related_name="notes")
    created_at = models.DateField()