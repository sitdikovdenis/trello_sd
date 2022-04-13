from django.urls import path

import auth_server.views as auth_server
from django.contrib.auth.views import LogoutView


app_name = 'auth_server'

urlpatterns = [
    path('signup/', auth_server.SignupView.as_view(), name='signup'),
    path('signup/register', auth_server.SignupView.as_view(), name='signup'),
    path('signup/confirmation/<confirmation_id>/', auth_server.SignupConfirmationView.as_view(), name='confirmation'),
]
