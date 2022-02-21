from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User

from auth_server.models import MirricoManagementUser2, Employee, RegisterVerificationCode


class MyAuthenticationForm(AuthenticationForm):
    surname = forms.CharField(label='Фамилия',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия', max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label='Имя', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    patronymic = forms.CharField(label='Отчество', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MirricoManagementUser2
        fields = ('first_name', 'last_name', 'patronymic', 'password1', 'password2',)

    def is_valid(self):
        name = self.data['first_name']
        surname = self.data['last_name']
        patronymic = self.data['patronymic']

        employees_qs = Employee.objects.filter(name=name, patronymic=patronymic, surname=surname)
        if employees_qs.count() == 0:
            self.errors['employee_signup_error'] = 'Сотрудник не работает в компании'
            return False
        if MirricoManagementUser2.objects.filter(employee=employees_qs[0]).count() > 0:
            self.errors['employee_signup_error'] = 'Сотрудник уже зарегистрирован'
            return False
        return True


class SignUpConfirmationForm(ModelForm):
    input_code = forms.CharField(label='Код', max_length=30, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RegisterVerificationCode
        fields = ['employee']
        widgets = {
            'code': forms.HiddenInput(attrs={'class': 'form-control'}),
            'employee': forms.HiddenInput(attrs={'class': 'form-control'}),
        }

    def is_valid(self):
        code = self.data['code']
        employee_id = self.data['employee_id']
        actual_code = RegisterVerificationCode.objects.filter(reg_ver_code_employee__id=employee_id).last()
        if actual_code is not None:
            if code == actual_code:
                return True
        return False
