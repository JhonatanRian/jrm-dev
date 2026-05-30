import django_filters
from django import forms
from django.db import connection
from django.db.models import Q

from blog.models import Post


class PostFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Buscar",
        })
    )

    class Meta:
        model = Post
        fields = ["search"]

    def filter_search(self, queryset, name, value):
        if not value:
            return queryset

        # Use native full-text search if PostgreSQL is the database
        if connection.vendor == "postgresql":
            from django.contrib.postgres.search import SearchQuery
            return queryset.filter(search_vector=SearchQuery(value))

        # Otherwise fallback gracefully to case-insensitive LIKE search
        return queryset.filter(
            Q(title__icontains=value) | Q(content__icontains=value)
        )
