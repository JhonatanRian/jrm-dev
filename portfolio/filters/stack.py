import django_filters
from django import forms

from portfolio.models import Stack


class StackFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Buscar",
            }
        ),
    )

    class Meta:
        model = Stack
        fields = ["name"]
