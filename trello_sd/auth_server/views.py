from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import redirect

from rest_framework.viewsets import ModelViewSet

from auth_server.models import Employee, SubDivision, RegisterVerificationCode
from auth_server.serializers import EmployeeSerializer, SubDivisionSerializer
from django.contrib.auth.views import LoginView
from auth_server.forms import MyAuthenticationForm, SignUpForm, SignUpConfirmationForm


class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.filter(state='Д')
    serializer_class = EmployeeSerializer


class SubDivisionModelViewSet(ModelViewSet):
    queryset = SubDivision.objects.all()
    serializer_class = SubDivisionSerializer


class SignupView(CreateView):
    form_class = SignUpForm
    success_url = 'login'
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        signup_form = SignUpForm(request.POST)
        context = {'form': signup_form}
        if signup_form.is_valid():
            data = request.POST
            name = data['first_name']
            surname = data['last_name']
            patronymic = data['patronymic']
            employee = Employee.objects.filter(name=name, patronymic=patronymic, surname=surname)[0]
            RegisterVerificationCode.objects.create(employee=employee)
            return redirect(f'confirmation/{employee.directum_id}', employee_id=employee.directum_id)
        else:
            if signup_form.errors['employee_not_found']:
                context['errors'] = signup_form.errors['employee_not_found']
        return render(
            request, 'register.html',
            context=context
        )


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form_class = MyAuthenticationForm


class SignupConfirmationView(View):
    def get(self, request, employee_id, *args, **kwargs):
        reg_ver_code = RegisterVerificationCode.objects.filter(employee__directum_id=employee_id).last()
        if reg_ver_code is None:
            raise Http404
        else:
            return render(
                request, 'confirmation.html',
                context={'form': SignUpConfirmationForm(instance=reg_ver_code)}
            )
