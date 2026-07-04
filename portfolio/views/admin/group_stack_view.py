from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

from core.views.mixins import AdminPermissionMixin
from portfolio.filters import GroupStackFilter
from portfolio.forms import GroupStackForm
from portfolio.models import GroupStack


class GroupStackListView(AdminPermissionMixin, FilterView):
    model = GroupStack
    queryset = GroupStack.objects.prefetch_related("stacks")
    template_name = "portfolio/admin/group_stack/group_stack_list.html"
    context_object_name = "group_stacks"
    filterset_class = GroupStackFilter
    paginate_by = 10


class GroupStackCreateView(AdminPermissionMixin, CreateView):
    model = GroupStack
    form_class = GroupStackForm
    template_name = "portfolio/admin/group_stack/group_stack_form.html"
    success_url = reverse_lazy("portfolio:group_stack_list")


class GroupStackUpdateView(AdminPermissionMixin, UpdateView):
    model = GroupStack
    form_class = GroupStackForm
    template_name = "portfolio/admin/group_stack/group_stack_form.html"
    success_url = reverse_lazy("portfolio:group_stack_list")


class GroupStackDeleteView(AdminPermissionMixin, DeleteView):
    model = GroupStack
    template_name = "portfolio/admin/group_stack/group_stack_confirm_delete.html"
    success_url = reverse_lazy("portfolio:group_stack_list")
