import django_filters
from portfolio.models import Project


class ProjectFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título")

    class Meta:
        model = Project
        fields = ["title"]
