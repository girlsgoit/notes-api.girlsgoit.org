from django.urls import path

from .views import index, note_details

urlpatterns = [
    path('', index, name='index'),

    path('notes/<int:note_id>', note_details, name = "note_details"),
]