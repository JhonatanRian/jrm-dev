# pyrefly: ignore [untyped-import]
from django.contrib.auth.views import LoginView
# pyrefly: ignore [untyped-import]
from django.urls import reverse_lazy

from accounts.forms import LoginForm


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("core:painel")
    form_class = LoginForm
