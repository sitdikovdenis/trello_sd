from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from rest_framework.viewsets import ModelViewSet

from auth_server.models import Employee, SubDivision, RegisterVerificationCode, MirricoManagementUser2
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
            reg_ver_code = RegisterVerificationCode.objects.create(employee=employee)

            mail_theme = f"Вы зарегистрировались на нашем СУПЕР САЙТЕ. Для продолжения перейдите по ссылке " \
                         f'http://127.0.0.1:8000/auth/signup/confirmation/{reg_ver_code.uuid} ' \
                         f'Код подтверждения {reg_ver_code.code}'

            c = send_mail('Подтверждение регистрации на СУПЕР САЙТЕ',
                          mail_theme,
                          'sdr_dev@mail.ru',
                          [employee.email],
                          fail_silently=False, )
            print(c)

            MirricoManagementUser2.objects.create_user(username=employee.directum_id, email=employee.email,
                                                       password=data['password1'], patronymic=patronymic,
                                                       employee=employee)

            return render(request, 'message.html', context={'message': "На ваш email отправлено письмо для "
                                                                       "подтверждения регистрации"})
        else:
            if signup_form.errors['employee_signup_error']:
                context['errors'] = signup_form.errors['employee_signup_error']
        return render(
            request, 'register.html',
            context=context
        )


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form_class = MyAuthenticationForm


class SignupConfirmationView(View):
    def confirm_user(self, confirmation_id):
        reg_ver_code = RegisterVerificationCode.objects.filter(uuid=confirmation_id).last()
        user_qs = MirricoManagementUser2.objects.filter(employee__directum_id=reg_ver_code.employee.directum_id)
        if user_qs.count() > 0:
            user_qs[0].confirmed = True
            user_qs[0].save()
            reg_ver_code.delete()

    def get(self, request, confirmation_id, *args, **kwargs):
        reg_ver_code = RegisterVerificationCode.objects.filter(uuid=confirmation_id).last()
        if reg_ver_code is None:
            raise Http404
        else:
            return render(
                request, 'confirmation.html',
                context={'form': SignUpConfirmationForm()}
            )

    def post(self, request, confirmation_id, *args, **kwargs):
        reg_ver_code = RegisterVerificationCode.objects.filter(uuid=confirmation_id).last()
        code = request.POST['input_code']
        if reg_ver_code.code == code:
            message = "Учетная запись подтверждена"
            self.confirm_user(confirmation_id)
        else:
            message = "Неправильный код!"

        return render(
            request, 'message.html',
            context={'message': message}
        )


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'index.html'
        )
