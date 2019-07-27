from django.contrib import admin
from .models import Note, NoteElement, GGITUser
# Register your models here.
admin.site.register(NoteElement)
admin.site.register(GGITUser)
admin.site.register(Note)

