from crispy_forms.helper import FormHelper
from crispy_neurobrutalist.layout import Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_error_title = "Por favor, corrija os seguintes erros:"
        self.helper.add_input(Submit("submit", "Fazer Login"))

