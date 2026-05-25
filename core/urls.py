from django.urls import include, path

from core.views import PainelView

app_name = "core"

urlpatterns = [
    path("", PainelView.as_view(), name="painel"),
]
