import django_filters

from blog.models import Tag


class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Nome")

    class Meta:
        model = Tag
        fields = ["name"]
