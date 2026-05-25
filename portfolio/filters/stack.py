import django_filters

from portfolio.models import Stack


class StackFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Nome")

    class Meta:
        model = Stack
        fields = ["name"]
