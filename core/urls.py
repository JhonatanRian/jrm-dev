from django.urls import path

from core.views import PainelView

app_name = "core"

urlpatterns = [
    path("", PainelView.as_view(), name="painel"),
]
