from django.urls import path

from .views import index, note_details, notes


urlpatterns = [
    path('', index, name='index'),
    path('notes/', note_list, name = 'note_list'),
    path('notes/<int:note_id>', note_details, name = "note_details"),
    path('users/', users, name = 'users'),
]
