from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect


class AdminPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin para views administrativas.
    Exige que o usuário esteja logado e que passe no teste de permissão (is_staff=True).
    """

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(
                self.request, "Você não tem permissão para acessar esta página."
            )
            # Redireciona para o login publico ou painel_administrativo
            return redirect("accounts:login")
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
