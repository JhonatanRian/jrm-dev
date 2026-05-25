from django.views.generic.base import TemplateView

from portfolio.models import Portfolio


class PortfolioView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        portfolio = (
            Portfolio.objects.select_related("section_hero")
            .prefetch_related("projects", "groups_stacks__stacks")
            .filter(active=True)
            .first()
        )
        kwargs["portfolio"] = portfolio
        return super().get_context_data(**kwargs)
