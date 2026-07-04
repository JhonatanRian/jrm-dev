import django_filters
from django import forms

from blog.models import Tag


class TagFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Buscar",
            }
        ),
    )

    class Meta:
        model = Tag
        fields = ["search"]
