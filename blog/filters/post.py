import django_filters
from django import forms
from django.db.models import Q, QuerySet

from blog.models import Post


class PostFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_search",
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Buscar",
            }
        ),
    )

    class Meta:
        model = Post
        fields = ["search"]

    def filter_search(self, queryset: QuerySet[Post], name, value):
        if not value:
            return queryset.filter()

        return queryset.filter(Q(title__icontains=value) | Q(content__icontains=value))
