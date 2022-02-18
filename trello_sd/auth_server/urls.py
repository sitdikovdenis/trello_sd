from django.urls import path

import auth_server.views as auth_server

app_name = 'auth_server'

urlpatterns = [
    path('login/', auth_server.login, name='login'),
    path('logout/', auth_server.logout, name='logout'),
    path('signup/', auth_server.signup, name='signup'),
]
