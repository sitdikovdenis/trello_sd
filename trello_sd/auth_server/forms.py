from django.contrib.auth.forms import AuthenticationForm

from .models import AppUser


class AppUserLoginForm(AuthenticationForm):
    class Meta:
        model = AppUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AppUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
