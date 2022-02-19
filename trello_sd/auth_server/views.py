from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from rest_framework.viewsets import ModelViewSet

from auth_server.models import Employee, SubDivision
from auth_server.serializers import EmployeeSerializer, SubDivisionSerializer
from django.contrib.auth.views import LoginView
from auth_server.forms import MyAuthenticationForm


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.filter(state='Д')
    serializer_class = EmployeeSerializer


class SubDivisionModelViewSet(ModelViewSet):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hh/login.html'
    form_class = MyAuthenticationForm