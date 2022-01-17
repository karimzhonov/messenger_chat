from django.urls import path
from .views import *
from .rest import ProfileRestView, UserRestView, FriendsRestView, AllProfilesRestView

urlpatterns = [
    path('', index, name='global_chet'),
    path('chats/', chat_list, name='chat_list'),
    path('friend_list/', friend_list, name='friend_list'),
    path('settings/', settings, name='settings'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('sign-up/', register, name='register'),
    path('chat/<int:user_id>/', chat, name='chat'),

    path('rest/search_profiles/<str:text>/', ProfileRestView.as_view()),
    path('rest/user/<int:pk>/', UserRestView.as_view()),
    path('rest/friends/<int:number>/', FriendsRestView.as_view()),
    path('rest/profiles/', AllProfilesRestView.as_view())
]
