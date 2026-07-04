from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings
from portfolio import views

urlpatterns = [
    path("", views.PortfolioView.as_view(), name="portfolio"),
    path("blog/", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("jrm/", include("core.urls")),
    path("jrm/", include("portfolio.urls")),
    path("jrm/blog/", include("blog.admin_urls")),
    path("accounts/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(debug_toolbar_urls())
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
