from django.urls import path

from .views import index, note_list, users, note_elements_list, note_details

urlpatterns = [
    path('', index, name='index'),
    path('notes/', note_list, name = 'note_list'),
    path('notes/<int:note_id>', note_details, name = "note_details"),
    path('note-elements', note_elements_list, name ="note_elements_list"),
    path('users/', users, name = 'users'),
]
