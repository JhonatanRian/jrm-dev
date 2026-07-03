import django_filters
from django import forms
from django.db import connection
from django.db.models import Q

from blog.models import Post, Tag


class PublicPostFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Buscar posts...",
            "id": "blog-search-input",
        })
    )
    tag = django_filters.ModelChoiceFilter(
        field_name="tags",
        queryset=Tag.objects.all(),
        to_field_name="slug",
        label="Tag",
        empty_label="Todas as tags",
    )

    class Meta:
        model = Post
        fields = ["search", "tag"]

    def filter_search(self, queryset, name, value):
        if not value:
            return queryset

        if connection.vendor == "postgresql":
            from django.contrib.postgres.search import SearchQuery
            return queryset.filter(search_vector=SearchQuery(value))

        return queryset.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )
