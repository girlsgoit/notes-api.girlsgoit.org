from django.db import models
from django.contrib.auth.models import AbstractUser

class GGITUser(AbstractUser):
    settings = models.TextField()

class Note (models.Model)   
    user = FK(User)
    created_at =DateField