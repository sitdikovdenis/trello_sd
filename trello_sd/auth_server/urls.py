from django.urls import path

import auth_server.views as auth_server
from django.contrib.auth.views import LogoutView

app_name = 'auth_server'

urlpatterns = [
    path('login/', auth_server.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', auth_server.SignupView.as_view(), name='signup'),
]
