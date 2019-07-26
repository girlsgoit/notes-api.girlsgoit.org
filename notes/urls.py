from django.urls import path

from .views import index, note_list

urlpatterns = [
    path('', index, name='index'),
    path('notes/', note_list, name = 'note_list'),
]