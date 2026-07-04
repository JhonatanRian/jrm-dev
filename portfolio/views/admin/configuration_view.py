from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from core.views.mixins import AdminPermissionMixin
from portfolio.forms import PortfolioForm
from portfolio.models import Portfolio, SectionHero


class ConfigurationView(AdminPermissionMixin, View):
    template_name = "portfolio/admin/configuration/configuration.html"

    def get_portfolio(self):
        portfolio = Portfolio.objects.filter(active=True).first()
        if not portfolio:
            hero, _ = SectionHero.objects.get_or_create(
                title="Jhonatan Rian",
                subtitle="Programador Backend",
                description="2 anos de experiência com foco em Python e ecossistema Linux.",
            )
            portfolio = Portfolio.objects.create(
                section_hero=hero,
                about="",
                linkedin="https://linkedin.com",
                github="https://github.com",
                active=True,
                contact_email="[EMAIL_ADDRESS]",
            )
        return portfolio

    def get(self, request, *args, **kwargs):
        portfolio = self.get_portfolio()
        form = PortfolioForm(instance=portfolio)
        return render(
            request, self.template_name, {"form": form, "portfolio": portfolio}
        )

    def post(self, request, *args, **kwargs):
        portfolio = self.get_portfolio()
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            messages.success(request, "Configurações do portfólio salvas com sucesso!")
            return redirect("portfolio:configuration")
        else:
            messages.error(
                request, "Erro ao salvar as configurações. Verifique os campos."
            )
        return render(
            request, self.template_name, {"form": form, "portfolio": portfolio}
        )
