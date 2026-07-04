import django_filters
from django import forms

from portfolio.models import GroupStack


class GroupStackFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Buscar",
            }
        ),
    )

    class Meta:
        model = GroupStack
        fields = ["title"]
