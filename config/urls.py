from debug_toolbar.toolbar import debug_toolbar_urls
# pyrefly: ignore [untyped-import]
from django.contrib import admin
# pyrefly: ignore [untyped-import]
from django.urls import include, path

from config import settings
from portfolio import views

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="portfolio"),
    path("admin/", admin.site.urls),
    path("jrm/", include("core.urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(debug_toolbar_urls())
