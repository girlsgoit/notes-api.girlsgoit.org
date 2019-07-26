from django.urls import path

from .views import index, note_list, users

urlpatterns = [
    path('', index, name='index'),
    path('notes/', note_list, name = 'note_list'),
    path('users/', users, name = 'users'),
]
