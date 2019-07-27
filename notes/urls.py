from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, note_list, users, note_elements_list, user_me, note_details,user_details, username_is_unique, publish_note, register, done_note, notes_public

urlpatterns = [
    path('', index, name='index'),
    path('notes/', note_list, name = 'note_list'),
    path('notes/<int:note_id>', note_details, name = "note_details"),
    path('note-elements', note_elements_list, name ="note_elements_list"),
    path('users/', users, name = 'users'),
    path('users/<int:user_id>', user_details, name= 'user_details'),
    path('users/is-unique',username_is_unique, name = 'username_is_unique' ),
    path('notes/<int:note_id>/publish',publish_note, name = 'publish_note' ),
    path('users/register', register, name= 'register'),
    path('users/login', obtain_auth_token, name='login'),
    path('users/me', user_me, name='user_me'),
    path('notes/public', notes_public, name= 'notes_public'),
    path('notes/<int:note_id>/done', done_note, name = 'done_note' ),
    
]
