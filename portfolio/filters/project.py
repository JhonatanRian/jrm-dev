import django_filters

from portfolio.models import Project


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ["title"]
