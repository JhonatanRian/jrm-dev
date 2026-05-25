import django_filters
from portfolio.models import GroupStack


class GroupStackFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="Título")

    class Meta:
        model = GroupStack
        fields = ["title"]
