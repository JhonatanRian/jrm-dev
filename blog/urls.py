from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    # ── Rotas Públicas ──────────────────────────────────────────────────────
    path("", views.BlogListView.as_view(), name="public_list"),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="public_detail"),
]
