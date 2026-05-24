# pyrefly: ignore [untyped-import]
from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    # pyrefly: ignore [bad-override]
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
